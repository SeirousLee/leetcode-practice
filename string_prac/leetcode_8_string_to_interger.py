'''
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
 

示例 1：

输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。
示例 2：

输入：s = "   -42"
输出：-42
解释：
第 1 步："   -42"（读入前导空格，但忽视掉）
            ^
第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   -42"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。
示例 3：

输入：s = "4193 with words"
输出：4193
解释：
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = False
        if s.startswith("-"):
            negative = True
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        result = 0
        for i in s:
            if '0' <= i and i <= '9':
                num = int(i)
                # 对于溢出的处理方式通常可以转换为 INT_MAX 的逆操作。比如判断某数乘以 10 是否会溢出，那么就把该数和 INT_MAX 除以 10 进行比较
                if (self.MAX_INT // 10 < result or (self.MAX_INT // 10 == result and num > 7)):
                    return self.MIN_INT if negative else self.MAX_INT
                else:
                    result = result * 10 + num
            else:
                break

        return result if not negative else -result


# 有限状态机(deterministic finite automaton, DFA)
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:

    def __init__(self):
        # 初始状态
        self.state = 'start'
        # 正负标记
        self.sign = 1
        self.ans = 0
        # 状态转移表
        self.table = {
            # key为状态，value为下一个状态，第一列是空格时的转移状态，第二列是正负符号转移状态，第三列是数字转移状态，第四列是其他字符转移状态
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    # 根据字符获取下一个要转移的状态，返回转移状态表中列（index）
    def status_transfer(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    # 计算数值
    def get(self, c):
        self.state = self.table[self.state][self.status_transfer(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution_DFA:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
            if automaton.state == 'end':
                break
        return automaton.sign * automaton.ans


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("   -42"))
    print(s.myAtoi("   -424193 with words"))
    print(s.myAtoi("words and 987"))
