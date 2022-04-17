'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right + 1)
                s.pop()

        backtrack([], 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)
