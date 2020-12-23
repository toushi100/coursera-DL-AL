# Uses python3
# 8
# Last Digit of the Sum of Squares of Fibonacci Numbers
# Problem Description
# Task. Compute the last digit of F 0 2 + F 1 2 + · · · + F n 2 .
import sys


def sum_fib( n):
    n = n % 30
    a = [0, 1]
    if n<=1:
        return n
    add = 0
    for i in range(2, n+1):
        sum = a[i - 1] + a[i - 2]
        a.append(sum)
        add = add+a[i] ** 2

    return (add+1) % 10


if __name__ == '__main__':
    inputs = sys.stdin.read()
    n = int(inputs)
    print(sum_fib( n))
