a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = a[0]
hech = []
sum = 0
for num in a:
    if sum > 0:
        sum = sum + num
        hech.append((num,sum>ans))
    else:
        sum = num
        hech.clear()
        hech.append((num,True))

    ans = max(ans, sum)
while True:
    if not hech[-1][1]:
        hech.pop()
    else:
        break

print(ans)
print([i for i in hech])

# class Solution:
#     def maxSubArray(self, nums):
#         ans = nums[0]
#         sum = 0
#         for num in nums:
#             if sum > 0:
#                 sum = sum + num
#             else:
#                 sum = num
#         ans = max(sum, ans)
#         return ans
#
#
# a = Solution()
# print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
