class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_index = {}
        for i in range(len(nums)):
            num = nums[i]
            val = target - num
            if val in hash_index.keys():
                return ([hash_index[val], i])
            hash_index[num] = i
