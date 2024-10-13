'''from collections import defaultdict
from math import gcd

def normalize_slope(dy, dx):
    if dx == 0:
        return (1, 0)  
    if dy == 0:
        return (0, 1)  
    sign = -1 if (dy < 0) != (dx < 0) else 1
    dy, dx = abs(dy), abs(dx)
    g = gcd(dy, dx)
    return (sign * dy // g, dx // g)

def solve(inputfile, outputfile):
    with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
        T = int(infile.readline().strip())  
        for t in range(1, T + 1):
            N = int(infile.readline().strip())  
            ants = [tuple(map(int, infile.readline().split())) for _ in range(N)]  

            if N == 2:
                outfile.write(f"Case #{t}: 0\n")
                continue

            max_collinear = 1

            for i in range(N):
                slopes = defaultdict(int)
                for j in range(N):
                    if i != j:
                        dx = ants[j][0] - ants[i][0]
                        dy = ants[j][1] - ants[i][1]
                        slope = normalize_slope(dy, dx)
                        slopes[slope] += 1

                max_collinear = max(max_collinear, max(slopes.values(), default=0) + 1)

            M = N - max_collinear
            outfile.write(f"Case #{t}: {M}\n")

input_file = 'input.txt'  
output_file = 'output.txt'  
solve(input_file, output_file)'''
def convex_hull(points):
    points = sorted(points)
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def min_moves_to_line(ants):
    N = len(ants)
    if N <= 2:
        return 0  

    hull = convex_hull(ants)
    num_on_hull = len(hull)

    return N - num_on_hull

def main():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        T = int(infile.readline().strip())  
        for case_number in range(1, T + 1):
            N = int(infile.readline().strip())  
            ants = [tuple(map(int, infile.readline().strip().split())) for _ in range(N)]  
            moves = min_moves_to_line(ants)  
            outfile.write(f"Case #{case_number}: {moves}\n") 


main()
