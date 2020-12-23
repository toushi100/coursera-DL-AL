# Uses python3
# 6
# Last Digit of the Sum of Fibonacci Numbers
# Problem Introduction
# The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers
import sys


def fibonacci_sum_naive(n):
    n  = n % 60
    if n <= 1:
        return n
    F=[0,1]

    for i in range(2,n+1):
        sum = F[i-1] + F[i-2]+1
        F.append(sum)
       # print(i,F[i], F[i]% 10)


    return F[i] % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
