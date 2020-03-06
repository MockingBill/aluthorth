for i in range(1,21):
    for j in range(1,34):
        for n in range(1,301):
            if (i+j+n)==100 and n%3==0 and (5*i+3*j+n/3)==100:
                print('巧克力:'+str(i)+' 水果糖:'+str(j)+' 口香糖:'+str(n))
                print('花费:' + str(i*5) + ' 花费:' + str(j*3) + ' 花费:' + str(n/3))
                print()