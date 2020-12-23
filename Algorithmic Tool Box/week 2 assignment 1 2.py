# Uses python3
#Last Digit of a Large Fibonacci Number
def calc_fib(n):
    F=[ 0 for x in range( n ) ]
    if n <= 1:
        return n-1
    else:
        F[0]=0
        F[1]=1
        for i in range(2,n):
            F[i]=(F[i - 1] + F[i - 2]) % 10
    return F[n-1]

n = int(input())+1
print(calc_fib(n))
