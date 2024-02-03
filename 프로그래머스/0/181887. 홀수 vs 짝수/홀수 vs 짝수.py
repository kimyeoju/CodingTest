def solution(num_list):
    even = 0
    odd = 0
    
    for idx, value in enumerate(num_list, start=1):
        if idx % 2 == 0:
            even += value
        else:
            odd += value
            
    return max(even, odd)