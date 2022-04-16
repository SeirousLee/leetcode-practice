'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from queue import Queue
from typing import List
from itertools import product

number_mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations_product(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        for i in digits:
            result.append(number_mapping[i])
        return ["".join(r) for r in product(*result)]

    def letterCombinations_violence(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = number_mapping[digits[0]]
        for i in digits[1:]:
            tmp = []
            for r in result:
                for j in number_mapping[i]:
                    tmp.append(r + j)
            result = tmp
        return result

    def letterCombinations_bfs(self, digits: str) -> List[str]:
        if not digits:
            return []
        q = [""]
        for d in digits:
            length = len(q)
            for _ in range(length):
                tmp = q.pop(0)
                for i in number_mapping[d]:
                    q.append(tmp + i)
        return q

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result=[]

        def backtrack(combination:List[str]):
            # 递归退出条件
            if len(combination)==len(digits):
                result.append("".join(combination))
            else:
                digit = digits[len(combination)]
                for i in number_mapping[digit]:
                    combination.append(i)
                    backtrack(combination)
                    # 回溯
                    combination.pop()
        backtrack([])
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.letterCombinations("2345")
    print(res)
