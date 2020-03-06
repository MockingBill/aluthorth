# 最大携带的重量
max_weight = ？
sweet = [{'v': ？, 'w': ？}, {'v': ？, 'w': ？}, {'v': ？, 'w': ？}, {'v': ？, 'w': ？},
         {'v': ？, 'w': ？},{'v': ？, 'w': ？}, {'v': ？, 'w': ？}]


# 对糖果按照单价进行排序
sweet.sort(key=lambda x: x['v'] / x['w'], reverse=True)
# 目前装入的糖的重量
totalW = 0
# 目前装入糖的价值
totalV = 0
for i in range(len(sweet)):
    if (totalW + sweet[i]['w']) <= max_weight:
        totalW += sweet[i]['w']
        totalV += sweet[i]['v']
    else:
        totalV += sweet[i]['v'] / sweet[i]['w'] * float(max_weight - totalW)
        break
print(totalV)
