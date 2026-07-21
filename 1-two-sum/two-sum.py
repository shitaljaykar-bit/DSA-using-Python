class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
            class Solution:
                def twoSum(self, nums: list[int], target: int) -> list[int]:
                  seen = {}  # maps value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            
        return []