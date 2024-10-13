import math

def solve_cases(test_cases):
    results = []
    
    for i, (N, P) in enumerate(test_cases, 1):
        P_new = 100 * (P / 100) ** ((N - 1) / N)
        increase = P_new - P
        results.append(f"Case #{i}: {increase:.12f}")
    return results

T = int(input()) 
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = solve_cases(test_cases)

for result in results:
    print(result)
