class Solution:
    def __init__(self):
        self.dictList = None
        self.visited = None

    def getSimmerWord(self, cuWord):
        res = []
        for i in range(len(cuWord)):
            worditem = list(cuWord)
            worditem[i] = '*'
            key = ''.join(worditem)
            # 选择未曾访问过的单词
            if key in self.dictList:
                for xi_word in self.dictList[key]:
                    if xi_word not in self.visited:
                        res.append(xi_word)
        return res

    def isSimmer(self, a, b):
        a = list(a)
        b = list(b)
        l_n = len(a)
        y = 0
        n = 0

        for i in range(l_n):
            if a[i] == b[i]:
                y = y + 1
            else:
                n = n + 1
        if y == (l_n - 1) and n == 1:
            return True
        else:
            return False

    def ladderLength(self, beginWord, endWord, wordList):
        wordList=list(set(wordList))
        quene = [(beginWord, 1)]
        self.dictList = {}
        for w in wordList:
            for k, v in enumerate(w):
                word = list(w)
                word[k] = '*'
                if ''.join(word) in self.dictList:
                    arr = []
                    arr.extend(self.dictList[''.join(word)])
                    arr.append(w)
                    self.dictList[''.join(word)] = arr
                else:
                    self.dictList[''.join(word)] = [w]
        self.visited = []

        while quene:
            curr_num = quene[0][1] + 1
            next_quen = self.getSimmerWord(quene[0][0])
            is_end = [q for q in quene if self.isSimmer(q[0], endWord)]
            if is_end:
                return is_end[0][1]+1
            else:
                self.visited.extend(next_quen)
                quene.extend([(k, curr_num) for k in next_quen])
                quene.remove(quene[0])
                if len(quene) <= 0:
                    return 0


beginWord,endWord=tuple(input().split())

wordList=input().split()
s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))
