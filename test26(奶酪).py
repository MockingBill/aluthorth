'''加入了负数的影响,主要考虑最后结果小于0的话直接返回0'''
'''当p小于0的话就不要加p了'''
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    p = nums[0]
    q = max(nums[0], nums[1])

    for i in range(2, n):
        if p>0:
            next_ = max(p + nums[i], q)
        else:
            next_ = max(nums[i], q)
        p, q = q, next_
    if q<0:
        return 0
    else:
        return q

n = int(input())
data = []
for i in range(n):
    num = int(input())
    data.append([int(i) for i in input().split()])
for i in data:
    print(rob(i))