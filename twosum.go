package main

import "fmt"
func twoSum(nums []int, target int) []int {
	hashTable :=map[int]int{}
	for i, num := range nums {
		if j,ok :=hashTable[target-num];ok{
			return []int{j,i}
		}
		hashTable[num]=i

	}

	return  nil
}

func main()  {
	target := 9
	nums := []int{2,7,11,15}
	res:=twoSum(nums,target)
	fmt.Println("res is %v",res)
}