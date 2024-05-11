def solution(numbers, k):
    n = len(numbers)
    current = 0

    for i in range(k - 1):
        current += 2

        if current >= n:
            current -= n

    return numbers[current]
