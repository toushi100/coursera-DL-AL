# Uses python3
import sys

def get_change(m):
    coins = [1,3,4]
    dp = [m+1]* (m+1)
    dp[0] = 0
    for i in range(1,m+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i],dp[i-coins[j]]+1)

    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))