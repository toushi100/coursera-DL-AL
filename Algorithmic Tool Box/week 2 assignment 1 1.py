# Uses python3
#Fibonacci Number
def calc_fib(n):
    F=[ 0 for x in range( n ) ]


    if n <= 1:
        return n-1
    else:
        F[0]=0
        F[1]=1
        for i in range(2,n):
            F[i]=F[i - 1] + F[i - 2]
    return F[n-1]

n = int(input())
n= n+1

print(calc_fib(n))
