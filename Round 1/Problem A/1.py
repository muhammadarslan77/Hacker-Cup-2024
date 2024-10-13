def solve(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readlines()

    T = int(data[0].strip())  # Number of test cases
    result = []

    index = 1
    for t in range(1, T + 1):
        N = int(data[index].strip())  # Number of stations
        index += 1

        min_speed = 0
        max_speed = float('inf')

        for i in range(1, N + 1):
            A, B = map(int, data[index].strip().split())  # Time window [A_i, B_i] for station i
            index += 1

            # Calculate speed bounds for this station
            lower_bound = i / B  # Min speed to reach station i within B_i seconds

            if A > 0:
                upper_bound = i / A  # Max speed to reach station i within A_i seconds
            else:
                upper_bound = float('inf')  # If A_i = 0, treat as infinite speed

            # Update global speed bounds
            min_speed = max(min_speed, lower_bound)
            max_speed = min(max_speed, upper_bound)

        # If the range is invalid, output -1
        if min_speed > max_speed:
            result.append(f"Case #{t}: -1")
        else:
            result.append(f"Case #{t}: {min_speed:.6f}")

    # Write results to output file
    with open(output_file, 'w') as f:
        f.write('\n'.join(result) + '\n')

solve('input.txt', 'output.txt')
