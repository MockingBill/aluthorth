def getSingleStr(a):
    a_ = a[-1::-1]
    flag = False
    for k in range(len(a_), 0, -1):
        for j in range(len(a_) - k, -1, -1):
            if a_[j:j + k] in a:
                if a_[j:j + k] in a:
                    print(a_[j:j + k])
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(input())
# [getSingleStr(i) for i in arr]

def getSingleStr(a):
    a_ = a[-1::-1]
    for k in range(len(a_), 0, -1):
        for j in range(len(a_) - k, -1, -1):
            if a_[j:j + k] in a:
                if a_[j:j + k] in a:
                    return a_[j:j + k]
print(getSingleStr("aacdefcaa"))

#
# N = int(input())
# def Dp(i,j):
#     if i >= j:
#       return 1
#     if dp[i][j] != -1:
#         return dp[i][j]
#     if s[i] != s[j]:
#         return 0
#     else:
#         dp[i][j] = Dp(i+1,j-1)
#         return dp[i][j]
# for i in range(N):
#     s = input()
#     L = len(s)
#     dp = [[-1 for i in range(L+ 1)] for j in range(L+1)]
#     Len = 1
#     start = 0
#     for i in range(L-1):
#         for j in range(i,L):
#             if Dp(i,j) == 1:
#                 if j-i+1 > Len:
#                     Len = j-i+1
#                     start = i
#     print(s[start:start+Len])

