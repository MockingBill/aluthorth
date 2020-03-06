def comZQ(p, e, i, d):
    step = d
    while True:
        if (step-p) % 23 == 0 and step!=0:
            break
        else:
            step = step + 1
    while True:
        if (step-e) % 28 == 0 and step!=0:
            break
        else:
            step = step + 23
    while True:
        if (step-i) % 33 == 0 and step!=0:
            break
        else:
            step = step + 23 * 28
    return step-d


data = []
while True:
    text = input()
    if text != "-1 -1 -1 -1":
        row = [int(i.strip()) for i in text.split() if i.strip() != ""]
        data.append(row)
    else:
        break

for k,row in enumerate(data):
    print("Case "+str(k+1)+": the next triple peak occurs in "+str(comZQ(row[0], row[1], row[2], row[3]))+" days.")
