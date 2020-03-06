weight = [8, 7, 2, 10, 1]
value = [412, 266, 591, 711, 80]
weight_most = 10
def bag_0_1(weight, value, weight_most):  # return max value
    num = len(weight)
    weight.insert(0, 0)  # 前0件要用
    value.insert(0, 0)  # 前0件要用

    bag = [[0 for j in range(weight_most+1)] for i in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, weight_most + 1):
            if weight[i] <= j:
                print(i,j,"bag[i - 1][j - weight[i]] + value[i]",bag[i - 1][j - weight[i]] + value[i],"与bag[i - 1][j]",bag[i - 1][j])
                bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
            else:
                bag[i][j] = bag[i - 1][j]
    return bag[-1][ -1]

result = bag_0_1(weight, value, weight_most)
print(result)