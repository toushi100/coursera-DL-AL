import sys

# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    temp1 , temp2 = 0 , 0
    for first in range(n):
        if numbers[first] >= temp1:
            temp1 = numbers[first]
            index = first

    for first in range(n):
        if numbers[first] >= temp2 and first != index:
            temp2 = numbers[first]
    max_product = temp1 * temp2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
