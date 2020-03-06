textarray=[]
try:
    while True:
        text=input().split()
        textarray.append(text)
except Exception as err:
    pass
for k,v in enumerate(textarray):
    textarray[k]=[int(i.strip()) for i in v]
p=textarray[0][1]
print(len([i for i in textarray[1] if i==p]))