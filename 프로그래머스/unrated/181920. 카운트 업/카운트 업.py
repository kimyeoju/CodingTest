def solution(start, end):
    answer = []
    for i in range(start,end+1):
        number = 0
        number += i
        answer.append(number)
    return answer