class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums)

        smallest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num
                num +=1 

        return smallest 