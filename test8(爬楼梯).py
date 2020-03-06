textarray = []
try:
    while True:
        textarray.append(int(input()))
except Exception as err:
    pass


def fib(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for n in textarray:
    print(fib(n))



