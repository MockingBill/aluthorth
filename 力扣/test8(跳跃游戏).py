class Solution:
    def canJump(self, nums):
        i = -2
        j = 1
        if len(nums)==1:
            return True
        if len([1 for i in range(len(nums)-1) if nums[i]==0])!=0:
            return False
        init_len = len(nums)
        while len(nums) >= 2 and j <= len(nums) and abs(i) <= len(nums):
            if nums[i] >= j:
                nums.pop()
            else:
                i = i - 1
                j = j + 1
        if len(nums) == init_len:
            return False
        else:
            return True
a=Solution()

print(a.canJump([0,2,3]))
