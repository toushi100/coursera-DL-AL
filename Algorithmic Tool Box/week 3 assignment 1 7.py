# Uses python3

import sys


def largest_number(a):

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            first = a[i] + (a[j])
            second = a[j] + (a[i])
            if int(first) < int(second):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp

    res = ""
    for x in a:
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
#5 9 4 6 1 9
#3 23 39 92
#2 21 2