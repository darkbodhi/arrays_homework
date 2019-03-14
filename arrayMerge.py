

def arraymerge(target, src1, src2):
    target = src1 + src2
    while n < len(target):
        while n < len(target):
            if target[n] <= target[n + 1]:
                a = target[n]
                b = target[n + 1]
                target[n] = b
                target[n + 1] = a
                n += 1
            else:
                return n == 0
    n += 1