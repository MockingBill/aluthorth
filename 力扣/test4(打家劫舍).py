class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        return self.robb(nums, len(nums) - 1)

    def robb(self, nums, n):
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0], nums[1])
        elif n >= 2:
            return max(self.robb(nums, n - 2) + nums[n], self.robb(nums, n - 1))
a=Solution()
c=[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print(a.rob(c))

# 循环
class Solution:
    # dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        p = nums[0]
        q = max(nums[0], nums[1])

        for i in range(2, n):
            next_ = max(p + nums[i], q)
            p, q = q, next_

        return q