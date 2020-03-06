from apyori import apriori
data = [['PFcREM','HTTP'],
        ['PFcREM','PFcREM','TCP','TCP'],
        ['PFcREM','TCP','HTTP','UDP'],
        ['PFcREM','TCP','HTTP','UDP'],
        ['PFcREM','TCP','HTTP','UDP']]

result = list(apriori(transactions=data))

for i in result:
    print(i.items,i.support)
    print(i.ordered_statistics[0].items_add)
    print(i.ordered_statistics[0].confidence)
    print("提升度",i.ordered_statistics[0].lift)
    print('-'*20)


frozenset()
