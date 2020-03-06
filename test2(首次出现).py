a=input()
a=[i for i in a]
s=[]
d={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
for c in a:
    if c in d:
        d[c]=d.get(c)+1
only1=[k for k,v in d.items() if v==1]
if len(only1)==0:
    print('no')
else:
    print(a[min([a.index(i) for i in only1])])