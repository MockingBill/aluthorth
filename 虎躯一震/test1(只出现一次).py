class Solution1(object):
    def singleNumber(self, nums):
        hash_table = {}
        '''出现两次就被删除掉了，出现一次就被记录下来了，当然，出现三次也会被记录下来'''
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        print(hash_table)
        return hash_table.popitem()[0]

class Solution2(object):
    def singleNumber(self, nums):
        """使用按位异或,因为异或满足结合律"""
        a = 0
        for i in nums:
            a ^= i
        return a




