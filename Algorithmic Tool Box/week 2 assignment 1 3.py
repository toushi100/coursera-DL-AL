# Uses python3
import sys
#Greatedt common devisor
def gcd_naive(bn, sn):
    r = 1
    while r !=0 :
        r = bn % sn
        bn = sn
        sn = r
    return bn

if __name__ == "__main__":
    input = sys.stdin.read()
    bn, sn = map(int, input.split())
    print(gcd_naive( bn, sn))