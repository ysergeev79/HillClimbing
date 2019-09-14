
from math import sin,cos, sqrt

import random



def f1(x, y):
    return sin(x/2) + cos(2*y)

def f2(x, y):
    return (-1 * abs(x - 2)) - abs((0.5 * y) + 1) + 3


#


def get_neighbor_values ( fnc, factor_size, x, y):

    factor = 0.70710678118
    neighbors = {}

    neighbors.append[fnc(x, y)] = (x, y)
    neighbors[fnc(x - step_size*factor, y - step_size*factor)] = (x - step_size*factor, y - step_size*factor)
    neighbors[fnc(x, y - step_size)] = (x, y - step_size)
    neighbors[fnc(x + step_size*factor, y - step_size*factor)] = (x + step_size*factor, y - step_size*factor)
    neighbors[fnc(x - step_size, y)] = (x - step_size, y)
    neighbors[fnc(x + step_size, y)] = (x + step_size, y)
    neighbors[fnc(x - step_size*factor, y + step_size*factor)] =  (x - step_size*factor, y + step_size*factor)
    neighbors[fnc(x + step_size*factor, y + step_size*factor)] = (x + step_size*factor, y + step_size*factor)

    maximum = max(neighbors.keys())
    return maximum, neighbors[maximum]



def hill_climbing(step_size, x, y, fnc):

        max = -10000000
        current_x = x
        current_y = y

        step_num = 0

        while True:
            max = fnc(current_x, current_y)
            given_max, (x_at_given_max, y_at_given_max) = get_neighbor_values(fnc, step_size, current_x, current_y)
            if max == given_max:
                # max has been hit
                return max, current_x, current_y, step_num
            else:
                max = given_max
                current_x = x_at_given_max
                current_y = y_at_given_max
                step_num = step_num + 1



def run_hill_climbing(fnc):
    # Step size in a tuple
    steps = [0.01, 0.05, 0.1, 0.2]

    result = {}

    for i in steps:
        result[i] = []
        for j in range(0,99):
            x = random.uniform(0,10)
            y = random.uniform(0,10)
            max, current_x, current_y, step_num = hill_climbing(i, x, y, fnc)
            result[i].append((max, step_num))

    return result


def get_average(result, input):
    steps = [0.01, 0.05, 0.1, 0.2]
    averages = {}
    for i in steps:
        averages[i] = []
        avg = 0
        for j in result[i]:
            avg = avg + j[input]
        avg = avg / 100
        averages[i].append(avg)
    return averages
def get_std(result, averages,  input):
    steps = [0.01, 0.05, 0.1, 0.2]
    stds = {}
    for i in steps:
        stds[i] = []
        std = 0
        avg = averages[i][0]
        for j in result[i]:
            std = std + ((j[input] - avg) ** 2)
        std = sqrt(std / 100)
        stds[i].append(std)
    return stds




results_f1 = run_hill_climbing(f1)
results_f2 = run_hill_climbing(f2)

averages_max_f1 = get_average(results_f1, 0)
averages_steps_f1 = get_average(results_f1, 1)
averages_max_f2 = get_average(results_f2, 0)
averages_steps_f2 = get_average(results_f2, 1)

sd_max_f1 = get_std(results_f1, averages_max_f1, 0)
sd_steps_f1 = get_std(results_f1, averages_steps_f1, 1)
sd_max_f2 = get_std(results_f2, averages_max_f2, 0)
sd_steps_f2 = get_std(results_f2, averages_steps_f2, 1)


print(averages_max_f1)

print(averages_steps_f1)

print(sd_max_f1)

print(sd_steps_f1)

print("\n")

print("Results of F2: ")

print(averages_max_f2)

print(averages_steps_f2)

print(sd_max_f2)

print(sd_steps_f2)

