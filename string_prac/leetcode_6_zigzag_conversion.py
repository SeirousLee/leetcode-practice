'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string_prac s, int numRows);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        str_list = [[] for i in range(numRows)]
        revert = False
        j = 0
        for i in s:
            if not revert:
                str_list[j].append(i)
                j += 1
            else:
                str_list[j].append(i)
                j -= 1
            if j == numRows:
                revert = True
                j = numRows - 2
            if j < 0:
                revert = False
                j = 1
        result = ''
        for s in str_list:
            result += ''.join(s)

        return result

if __name__ == '__main__':
    s=Solution()
    res = s.convert('PAYPALISHIRING',3)
    print(res)
