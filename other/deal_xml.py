import requests
from bs4 import BeautifulSoup
data=[]
with open("server") as file:
    for line in file.readlines():
        if line.startswith("<server"):
            line=line.replace("\"","")
            line = line.replace("/>", "")
            array=line.split()
            del array[0]
            map={}
            for item in array:
                i=item.split("=")
                if len(i)==2:
                    map[i[0]]=i[1]
            data.append(map)
i=0
for item in data:
    if item['country']=="China":
        try:
            resu=requests.get("http://"+item['host'])
            soup=BeautifulSoup(resu.content,'html.parser')
            if soup.p.text=="It worked!":
                print(item)
                i+=1
        except Exception as e:
            print("err")
print(i)


