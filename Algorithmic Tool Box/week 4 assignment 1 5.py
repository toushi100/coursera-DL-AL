# Uses python3
import sys

def fast_count_segments(starts, ends, points,i,cnt):
    if i == len(starts):
        return cnt
    for j in range(len(points)):

        if starts[i] <= points[j] <= ends[i]:
            cnt[j] += 1

    fast_count_segments(starts,ends, points,i+1,cnt)

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    count = [0] * len(points)

    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt2 = fast_count_segments(starts, ends, points,0,count)
    for x in  cnt2:
        print(x, end=' ')

#2 3 0 5 7 10 1 6 11
#1 3 -10 10 -100 100 0
#3 3 0 5 2 5 6 7  1 4 8
#3 2 0 5 -3 2 7 10 1 6