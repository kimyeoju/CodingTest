def solution(myString):
    answer = ''
    for i in myString:
        answer += i.lower()
        answer = answer.replace('a','A')
    return answer