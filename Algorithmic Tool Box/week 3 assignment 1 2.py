# Uses python3
import sys


def fractionalknapsack(capacity, weights, values):
    curr_weight = 0
    curr_value = 0
    print(capacity)
    print(weights)
    print(values)



    for i in range(n):
        if curr_weight + weights[i] <= capacity:
            curr_weight += weights[i]
            curr_value += weights[i]
        else:
            accomodate = weights[i] - curr_weight
            value_added = values[i] * (accomodate / weights[i])
            curr_value += value_added
            break

    return curr_value



    if capacity == 0:
        return 0
    for i in range(n):
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            available_weights = min(capacity, weights[max_index])
            value = value + available_weights * values[max_index]/weights[max_index]
            weights[max_index] = weights[max_index] - available_weights
            capacity = capacity - available_weights

    return value
def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(n):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i]/weights[i]
            index = i
    return index

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = fractionalknapsack(capacity, weights, values)
    print("{:.10f}".format(opt_value))

