


def spileArr(a, n):
    if n in a:
        nums = 0
        for j in list(a):
            if n == j:
                nums = nums + 1
        return a.replace(n * nums, '')
    else:
        return ''


def do(s):
    if s == '':
        return
    print(set(list(s)))
    for w in set(list(s)):
        do(spileArr(s, w))
do('28977694')
