class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenList = len(nums)
        first = 0
        last = lenList
        mid = ((first + last) // 2)
        #checking to see if the list is sorted or not
        if (nums[0] > nums[lenList-1]):
            while True:
                if nums[mid] < nums[first]:
                    last = mid
                elif nums[mid] > nums[first]:
                    first = mid
                elif nums[mid] == nums[first]:
                    break
                mid = ((first + last) // 2)
        else:
            return nums[first]
        return nums[last]





        