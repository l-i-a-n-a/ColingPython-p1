def solution(n):
    numbers = []
    a = 1
    while True:
        numbers.append(a)
        a += a
        if a > n:
            break
    return numbers