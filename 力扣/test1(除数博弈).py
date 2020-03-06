class Solution:
    def __init__(self):
        self.times = 0
    def divis(self, num):
        for n in range(1, num, 1):
            if n == num or n == 0:
                return 0
            elif num % n == 0:
                self.times = self.times + 1
                self.divis(num - n)
                break
            else:
                pass

    def divisorGame(self, N):
        self.divis(N)
        return (self.times % 2 == 1)

