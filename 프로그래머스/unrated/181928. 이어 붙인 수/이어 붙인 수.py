def solution(num_list):
	# 홀수 저장 odd
    odd = ""
    # 짝수 저장 even
    even = ""
    
    answer = 0
    
    for i in num_list:
        # 짝수일 때
        if i % 2 == 0:
            even += str(i)
        # 홀수일 때
        else:
            odd += str(i)
            
    answer = int(even)+ int(odd)
    return answer
            