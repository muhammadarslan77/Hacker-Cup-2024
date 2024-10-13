def solve_from_file(file_name, output_file_name='output.txt'):
    with open(file_name, 'r') as file:
        data = file.readlines()

    index = 0
    T = int(data[index].strip())  
    index += 1
    
    results = []
    
    for t in range(1, T + 1):
        N, K = map(int, data[index].split())  
        index += 1
        S = [int(data[i].strip()) for i in range(index, index + N)]  
        index += N
        
        
        S.sort()
        
        total_time = 0
        
        while N > 3:
            option1 = S[1] + S[0] + S[N - 1] + S[1]  
            option2 = S[N - 1] + S[N - 2] + 2 * S[0]  
            
            total_time += min(option1, option2)
            N -= 2  
            
        if N == 3:
            total_time += S[2] + S[1] + S[0]  
        elif N == 2:
            total_time += S[1]  
        elif N == 1:
            total_time += S[0] 

        if total_time <= K:
            results.append(f"Case #{t}: YES")
        else:
            results.append(f"Case #{t}: NO")
    
    with open(output_file_name, 'w') as output_file:
        for result in results:
            output_file.write(result + '\n')
    print(f"Results successfully written to {output_file_name}")

solve_from_file('input.txt')
