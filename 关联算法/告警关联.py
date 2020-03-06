# 先安装pandas、apyori两个外部包
# pip install apyori==1.1.1
# pip install pandas



import pandas as pd
import math
from apyori import apriori
# 读取excel数据
sn_warm_data = pd.read_excel("./告警数据.xlsx")
# 用于计算分组时的进度
num = 0
all_gr_data = []


# 该函数作用于分组后的数据，将告警发生时间小于60秒的分到一个数组里。
# all_gr_data用于存放相距60秒内的告警
def fiest_apply(row):
    global num
    num = num + len(row)
    dict_group = {}
    compire = None
    row = row.sort_values('TIME_OF_ALARM')
    for x in range(len(row.index)):
        if compire == None:
            compire = x
            continue
        else:
            Difference_Value = row.iloc[x]['TIME_OF_ALARM'] - row.iloc[compire]['TIME_OF_ALARM']
            if Difference_Value.seconds <= 60:
                if dict_group.get(compire) == None:
                    dict_group[compire] = []
                    dict_group[compire].append(row.iloc[compire])
                    dict_group[compire].append(row.iloc[x])
                    continue
                elif dict_group.get(compire) != None:
                    dict_group[compire].append(row.iloc[x])
                    continue
            else:
                compire = x
                continue
    if num % 500 == 0:
        nm = int(math.ceil((num / 20000) * 40))
        print(nm * "-" + ">", str(round(num * 100 / 20000, 2)) + "%")
    all_gr_data.append(dict_group)
    return None


# 按照网元名称进行分组
sn_warm_data.groupby(['NETWORK_ELEMENT_NAME']).apply(fiest_apply)
new_all_gr_data = []
# 将集合中的空数组去掉
for k, v in enumerate(all_gr_data):
    if len(v) > 0:
        new_all_gr_data.append(v)
# 将集合中的标题列汇总到一个数组中用于apriori计算
apro = []
for i in all_gr_data:
    for k, v in i.items():
        d = []
        for vv in v:
            d.append(vv['TITLE'])
        apro.append(d)

results = list(apriori(apro, min_confidence=0.01, min_support=0.01, min_lift=1))
# 满足设定最小参数的的集合
# 其中当集合中元素大于2时，不同元素组合具备不同的置信度和提升度，但是支持度都一样
# 支持度：集合中元素同时出现的概率
# 置信度：items_base出现的前提下出现items_add的概率
# 提升度：包含items_add同时包含items_base的概率
# 提升度大于等于1才有意义
for k, v in enumerate(results):
    # 只看有两个及以上元素的关联集合。单独一个元素的集合没有意义。
    if len(v.items) >= 2:
        print(v.items)
        print("支持度:", v.support)
        for j in results[k].ordered_statistics:
            print(list(j.items_base), list(j.items_add), "置信度:", j.confidence, "提升度:", j.lift)
        print("-" * 10)
