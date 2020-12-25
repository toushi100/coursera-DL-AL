# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    arr = [0 for _ in range(n)]
    for i in range(n):
        if capacity == 0:
            return value
        arr[i] = values[i] / weights[i]
        arr.sort(reverse=True)

    print(arr)

    return value


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


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = fractionalknapsack(capacity, weights, values)
    print("{:.10f}".format(opt_value))
