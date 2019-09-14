
from math import sin,cos, sqrt
from operator import itemgetter
import random
import statistics as sts


def f1(x, y):
    return sin(x/2) + cos(2*y)

def f2(x, y):
    return (-1 * abs(x - 2)) - abs((0.5 * y) + 1) + 3





def get_beam_neighbor_values ( fnc, step_size, x, y, neighbors):

    factor = 0.70710678118

    neighbors.append((x,y,fnc(x, y)))
    neighbors.append((x+step_size,y,fnc(x+step_size, y)))
    neighbors.append((x+step_size*factor, y+step_size*factor,fnc(x+step_size*factor, y+step_size*factor)))
    neighbors.append((x, y+step_size,fnc(x, y+step_size)))
    neighbors.append((x-step_size*factor, y+step_size*factor,fnc(x-step_size*factor, y+step_size*factor)))
    neighbors.append((x-step_size,y,fnc(x-step_size, y)))
    neighbors.append((x-step_size*factor, y-step_size*factor,fnc(x-step_size*factor, y-step_size*factor)))
    neighbors.append((x, y-step_size,fnc(x, y-step_size)))
    neighbors.append((x+step_size*factor, y-step_size*factor,fnc(x+step_size*factor, y-step_size*factor)))


def local_beam_search(fnc, step_size, temp1, temp2, width):
    k_num_child = []
    step_num = 0



    neighbors = []

    while True:

        mean = sts.mean(map(lambda x: x[2], k_num_child))
        for (curr_x, curr_y, _) in k_num_child:
            get_beam_neighbor_values(fnc, step_size, curr_x, curr_y, neighbors)

        k_num_child = sorted(neighbors, key=itemgetter(2))[-width:]

        if mean == sts.mean(map(lambda x: x[2], k_num_child)):
            (top_x, top_y, top_z) = k_num_child [-1:][0]
            return top_z, top_x, top_y, step_num

    else:
        step_num = step_num + 1



#Returns list of averages for each step_size. Mode = 1 is average max. Mode = 2 is average steps to convergence.
#Index 0 = step_size 0.01, 1 = 0.05, 2 = 0.1, 3 = 0.2
def get_stats(fnc):
    step_size = [0.01, 0.05, 0.1, 0.2]

    beam_width = [2, 4, 8, 16]

    neighbors = {}

    # gather data
    for i in step_size:
        neighbors[i] = {}

        for width in beam_width:

            neighbors[i][width] = []
            for i in range(0, 99):
                x = random.uniform(0, 10)
                y = random.uniform(0, 10)

                max, curr_x, curr_y, step_num = local_beam_search(fnc, i, x, y, width)
                # print("highest point of fnc found")
                # print("height: "+str(hn)+", x: "+str(hx)+", y: "+str(hy)+", at step "+str(s_n))

                neighbors[i][width].append(max)




    stats = {}
    for i in step_size:
        stats[i] = {}
        for width in beam_width:
            stats[i][width] = (sts.mean(neighbors[i][width]), sts.stdev(neighbors[i][width]))

    return stats



stats_f1 = get_stats(f1)
stats_f2 = get_stats(f2)

print("Results of F1: ")

print(stats_f1)
print("\n")
print("Results for f2: ")
print("\n")
print(stats_f2)


