# 3 5 4
V_max = [3, 5]
n = 4
V = [0, 0]


def do(pos, op):

    if V[pos] == 4:
        return
    # 装满
    elif op == 'FILL':
        V[pos] = V_max[pos]
    # 倒完
    elif op == 'DROP':
        V[pos] = 0
    # A倒入B
    elif op == 'POUR':
        V[pos] = 0
        if pos == 0:
            V[pos + 1] = min(V_max[pos + 1], V[pos + 1] + V[pos])
        else:
            V[pos - 1] = min(V_max[pos - 1], V[pos - 1] + V[pos])
do(0,'FILL')
print(V)

