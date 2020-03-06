# 巧克力购买的数量范围
chocolate = [1, 20]
# 水果糖购买的数量范围
fruitCandy = [1, 33]
# 口香糖购买的数量范围
chewingGum = [1, 300]
# 所需要的糖果数量
required_num = 100
# 所需要话费的钱
required_money = 100
for i in range(chocolate[0], chocolate[1] + 1):
    for j in range(fruitCandy[0], fruitCandy[1] + 1):
        for n in range(chewingGum[0], chewingGum[1] + 1):
            if(i + j + n)==required_num and n % 3 == 0 and (5 * i + 3 * j + n / 3)==required_money:
                print('巧克力:' + str(i) + ' 水果糖:' + str(j) + ' 口香糖:' + str(n))
                print('花费:' + str(i * 5) + ' 花费:' + str(j * 3) + ' 花费:' + str(n / 3))
                print()
