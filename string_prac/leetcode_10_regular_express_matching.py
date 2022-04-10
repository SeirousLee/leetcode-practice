'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            # . 表示任意字符都匹配
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # dp[i][j]表示s的前i个字符是否与p的前j个字符是否匹配
                    # 当*表示0个匹配是dp[i][j]是否匹配与dp[i][j - 2]相关
                    dp[i][j] = dp[i][j - 2]
                    # 匹配到1个或多个是dp[i][j]是否匹配与dp[i-1][j]相关，因为* 是0个或多个匹配，所以使用|=
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    # 当不含*时，dp[i][j]的匹配性只与dp[i - 1][j - 1]相关
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]

if __name__ == '__main__':
    s=Solution()
    res = s.isMatch("aaa", "ab*a*c*a")
    print(res)
