T = int(input())
res = []
for k in range(T):
    N = int(input())
    data = input().split()
    min_word = data[0]
    min_score = int(data[1])
    for i in range(N * 10 - 1):
        data = input().split()
        if int(data[1]) < min_score:
            min_word = data[0]
            min_score = int(data[1])
        if min_word == data[0]:
            min_score = (min_score + int(data[1])) / 2

    res.append((min_word, min_score))
for i in res:
    print(i[0],i[1])
