import re

def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        babbling[i] = re.sub('aya|ye|woo|ma', '', babbling[i])

    answer = babbling.count('')
    return answer