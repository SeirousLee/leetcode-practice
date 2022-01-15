import "fmt"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	len1 := len(nums1)
	len2 := len(nums2)
	if len1 > len2 {
		return findMedianSortedArrays(nums2, nums1)
	}
	index := (len1 + len2 + 1) / 2
	left := 0
	right := len1
	for left < right {
		mid := (left + (right-left+1)/2)
		second_sep := index - mid
		if nums1[mid-1] > nums2[second_sep] {
			right = mid - 1
		} else {
			left = mid

		}
	}
	sep := index - left
	nums1_left_max := 0
	if left == 0 {
		nums1_left_max = math.MinInt32

	} else {
		nums1_left_max = nums1[left-1]
	}
	nums1_right_min := 0
	if left == len1 {
		nums1_right_min = math.MaxInt32

	} else {
		nums1_right_min = nums1[left]
	}
	nums2_left_max := 0
	if sep == 0 {
		nums2_left_max = math.MinInt32

	} else {
		nums2_left_max = nums2[sep-1]
	}
	nums2_right_min := 0
	if sep == len2 {
		nums2_right_min = math.MaxInt32

	} else {
		nums2_right_min = nums2[sep]
	}

	if (len1+len2)%2 == 1 {
		return float64(max(nums1_left_max, nums2_left_max))
	} else {
		return float64((max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min))) / 2.0
	}

}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

