class Solution:
    def sortColors(self, nums):
        r=[]
        w=[]
        b=[]
        for i in nums:
            if i==0:
                r.append(i)
            elif i==1:
                w.append(i)
            elif i==2:
                b.append(i)
            else:
                pass
        for i in w:
            r.append(i)
        for i in b:
            r.append(i)
        nums=r
        return r
a=Solution()
print(a.sortColors([2,0,2,1,1,0]))
