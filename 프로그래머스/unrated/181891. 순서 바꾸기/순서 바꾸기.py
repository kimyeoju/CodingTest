def solution(num_list, n):
    answer = []
    element = num_list[n:] + num_list[:n]
    answer += element
    return answer