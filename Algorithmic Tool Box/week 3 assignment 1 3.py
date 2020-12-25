# python3
import sys

'''
def compute_min_refills(distance, tank,n, stops):
    count=0
    start = 0
    stops.append(distance)
    for i in range(len(stops)):
        if distance > tank+ start:
            if tank + stops[i-1] < stops[i]:
                return -1
            if tank < stops[i]:
                start = stops[i-1]
                count += 1


    return count
'''


def compute_min_refills(distance, tank, n, stops):
    numrefills = 0
    currentrefill = 0
    limit = tank
    while limit < distance:
        while currentrefill < n -1 and stops[currentrefill + 1] <= limit:
            currentrefill += 1
        if currentrefill >= n or stops[currentrefill] > limit:
            return -1
        numrefills += 1  # Stop to tank
        limit = stops[currentrefill] + tank  # Fill up the tank
        currentrefill += 1
    return numrefills
'''
def compute_min_refills(dist,miles,n,gas_stations):
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank
        curr_refill += 1
    return num_refill
'''
if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))

# 950 400 4 200 375 550 750
# 10 3 4 1 2 5 9

# 700 200 4 100 200 300 400
# 200 250 2 100 150
# 750 400 3 200 375 550
# 5 1 4 1 2 3 4
