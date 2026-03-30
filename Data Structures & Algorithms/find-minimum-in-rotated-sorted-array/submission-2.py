class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]: #Minimum is on the right side
                left +=1

            else:
                right = mid #Minimum is on the left side

        return nums[left]        