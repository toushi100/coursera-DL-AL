# Uses python3
# 7
# Last Digit of the Sum of Fibonacci Numbers Again
# Problem Introduction
# Now, we would like to find the last digit of a partial sum of Fibonacci numbers
import sys

def sum_fib(m,n):
    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i-1] + a[i-2])
    m = m % 60
    n = n % 60
    if n < m:
        n += 60

    su = 0
    for j in range(m, n+1):
        su += a[j % 60]

    return su % 10


if __name__ == '__main__':
    inputs = sys.stdin.read()
    m, n = map(int, inputs.split())
    print(sum_fib(m, n))
