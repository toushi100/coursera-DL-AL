# Uses python3
# least common multiple
import sys


def lcm_naive(bn, sn):
    r = 1
    obn = bn
    osn = sn
    while r != 0:
        r = bn % sn
        bn = sn
        sn = r
    return int((obn*osn)/bn)



def lcm_naie(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


if __name__ == '__main__':
    input = sys.stdin.read()
    bn, sn = map(int, input.split())
    print(lcm_naive(bn, sn))
    #print("the solution " , lcm_naie(bn, sn))
