class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range (len(nums)):
            partner = target - nums[i]

            #if not equal to 0 this means we found the partner!
            if partner in seen:
                return [seen[partner], i]
            #if partner not found we just add this element to the dict
            else:
                seen[nums[i]] = i