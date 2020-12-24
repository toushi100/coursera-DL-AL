# Uses python3
#1
#Money Change
#Problem Introduction
#In this problem, you will design and implement an elementary greedy algorithm
#used by cashiers all over the world millions of times per day.
#Problem Description
#Task. The goal in this problem is to find the minimum number of coins needed to change the input value
#(an integer) into coins with denominations 1, 5, and 10.
import sys


def sum_fib( n):
    count = 0
    while n > 0:
        if n >= 10:
            n = n-10
            count += 1
        elif n >= 5:
            n = n - 5
            count += 1
        else :
            n = n -1
            count += 1
    return count


if __name__ == '__main__':
    inputs = sys.stdin.read()
    n = int(inputs)
    print(sum_fib( n))
