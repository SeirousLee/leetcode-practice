from typing import List
import sys


class Solution:
    # 二分查找
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 为了保证第一个数组比第二个数组小或者相等
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        len1 = len(nums1)
        len2 = len(nums2)
        # 分割线左边的所有元素需要满足的个数m + (n - m + 1) / 2;
        # 两个数组长度之和为偶数时，当在长度之和上 +1时，由于整除是向下取整，所以不会改变结果
        #  两个数组长度之和为奇数时，按照分割线的左边比右边多一个元素的要求，此时在长度之和上 + 1，就会被2整除，会在原来的数
        #  的基础上 + 1，于是多出来的那个1就是左边比右边多出来的一个元素
        index = (len1 + len2 + 1) // 2

        # 在nums1的区间[0, leftLength]里查找恰当的分割线，
        # 使得nums1[i - 1] <= nums2[j] & & nums2[j - 1] <= nums1[i]
        left = 0
        # 分割线可能在数组最后
        right = len1

        # nums1[i - 1] <= nums2[j]
        # 此处要求第一个数组中分割线的左边的值不大于(小于等于)第二个数组中分割线的右边的值
        # nums2[j - 1] <= nums1[i]
        # 此处要求第二个数组中分割线的左边的值不大于(小于等于)第一个数组中分割线的右边的值
        # 循环条件结束的条件为指针重合，即分割线已找到
        while left < right:
            # 二分查找，此处为取第一个数组中左右指针下标的中位数，决定起始位置
            # 此处+1首先是为了不出现死循环，即left永远小于right的情况
            # left和right最小差距是1，此时下面的计算结果如果不加1会出现mid一直=left的情况，而+1之后mid才会=right
            # 于是在left=mid的时候可以破坏循环条件，其次下标+1还会保证下标不会越界，因为+1之后向上取整，保证了
            # mid不会取到0值，即mid-1不会小于0
            # 此时mid也代表着在一个数组中左边的元素的个数
            mid = (left + right + 1) // 2
            # 第一个数组中左边的元素个数确定后，用左边元素的总和-第一个数组中元素的总和=第二个元素中左边的元素的总和
            # 此时second_sep就是第二个元素中左边的元素的个数
            second_sep = index - mid
            # 比较当前第一个数组分割线左侧数据是否满足小于或等于第二个数组分割线右侧的值
            # 如果不满足，则说明分割线需要往左移，否则分割线继续右移，
            # 因为可能当前第二个数组分割线左侧的值大于第一个数组分割线右侧的值，要取到临界点，所以继续移动，直到不能移动时
            if nums1[mid - 1] > nums2[second_sep]:
                right = mid - 1
            else:
                left = mid
        second_sep = index - left
        # 考虑到分割线可能在数组最开端即left=0，
        # 当left为0时，即可将左侧值赋值为最小整数，这样与第二个数组分割线左侧比较较大值时会选择第二个数组分割线左侧的值
        num1_left_max = nums1[left - 1] if left != 0 else -sys.maxsize - 1
        # 当分割线为数组最右端时，即left=len1
        # 此时可将分割线右侧值设定为最大整数值，这样与第二个数组分割线右侧比较较小值是会选择第二个数组分割线右侧的值
        nums1_right_min = nums1[left] if left != len1 else sys.maxsize
        nums2_left_max = nums2[second_sep - 1] if second_sep != 0 else -sys.maxsize - 1
        nums2_right_min = nums2[second_sep] if second_sep != len2 else sys.maxsize
        # 当数组长度之和为奇数时，只需取到两个数组分割线左侧的最大值即可
        if (len1 + len2) % 2 == 1:
            return max(num1_left_max, nums2_left_max)
        # 当数组长度之和为偶数时，需要取到中间两个数，即分割线左侧最大值和分割线右侧最小值，求和取平均值
        else:
            return (max(num1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
    
    # 双指针
    def findMedianSortedArrays_pointer(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        flag = True
        if (len1 + len2) % 2 == 1:
            flag = False
        print(flag)
        index = (len1 + len2) // 2
        i = 0
        j = 0
        count = -1
        median = 0
        while i < len1 or j < len2:
            if i == len1:
                tmp = nums2[j]
                j += 1
            elif j == len2:
                tmp = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    tmp = nums1[i]
                    i += 1
                else:
                    tmp = nums2[j]
                    j += 1
            count += 1
            if flag:
                if count == index - 1:
                    median = tmp
                if count == index:
                    median += tmp
                    median /= 2
                    return median
            else:
                if count == index:
                    return tmp


if __name__ == '__main__':
    nums1 = [1]
    nums2 = []
    s = Solution()
    s.findMedianSortedArrays_pointer(nums1, nums2)
