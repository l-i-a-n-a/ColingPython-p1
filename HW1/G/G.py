def solution(a, b):
    c = []
    for k in b:
        if k not in a:
            c.append(k)
    c = a + c
    c.sort()
    return c
