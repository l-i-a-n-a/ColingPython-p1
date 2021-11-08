def solution(n,k):
    numbers = list(range(1, n+1))
    m = 0
    while len(numbers) != 1:
        for x in range(len(numbers)):
            m += 1
            if m == k:
                del numbers[x]
                numbers = numbers[x:] + numbers[:x]
                m = 0
                break
    return numbers[0]
