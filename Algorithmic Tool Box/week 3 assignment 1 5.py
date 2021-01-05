# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments.sort(key = lambda segments: segments[1])
    points.append(segments[0].end)
    i = 0
    while i < len(segments):
        if segments[i].start <= points[-1] <= segments[i].end:
            del segments[i]
        else:
            points.append(segments[i].end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

# 3 1 3 2 5 3 6
# 4 4 7 1 3 2 5 5 6
