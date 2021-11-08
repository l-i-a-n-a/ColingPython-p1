def solution(x):
    l = len(x)
    if 'h' in x:
        amount_h = x.count('h')
        n = 0
        for k in range(l):
            if x[k] == 'h':
                n += 1
                if n > 1 and n < amount_h:
                    x = x[:k] + 'H' + x[k+1:]
                    l = len(x)
                else:
                    continue
    m = ''
    for k in range(len(x)):
        if k == 0 or k % 3 != 0:
            m = m +x[k]
    x = m
    l = len(x)
    while True:
        if '1' in x:
            for k in range(l):
                if x[k] == '1':
                    x = x[:k] + 'one' + x[k+1:]
                    l = len(x)
        else:
            break
    return x

