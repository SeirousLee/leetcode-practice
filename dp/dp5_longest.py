"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if not s:
        #     return s
        # dp=[""]*len(s)
        # dp[0]=s[0]
        # for i in range(1,len(s)):
        #     if s[i]==s[i-1] and len(set(dp[i-1]))==1:
        #         dp[i]=dp[i-1]+s[i]
        #     elif i-1-len(dp[i-1])>=0 and s[i-len(dp[i-1])-1] == s[i]:
        #         dp[i]=s[i]+dp[i-1]+s[i]
        #     else:
        #         dp[i]=s[i]
        # max_len=""
        # for i in dp:
        #     if len(max_len)<len(i):
        #         max_len=i
        # return max_len

        # 二维dp
        if len(s) < 2:
            return s
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        length = 0
        start, end = 0, 0
        for i in range(len(s)):
            dp[i][i] = True
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    if j - i + 1 > length:
                        length = j - i + 1
                        start = i
                        end = j
        return s[start:end + 1]

        # start,end=0,0
        # for i in range(len(s)):
        #     left_1,right_1=self.expand(s,i,i)
        #     left_2,right_2=self.expand(s,i,i+1)
        #     if right_1-left_1>end-start:
        #         start,end=left_1,right_1
        #     if right_2-left_2>end-start:
        #         start,end=left_2,right_2
        # return s[start:end+1]