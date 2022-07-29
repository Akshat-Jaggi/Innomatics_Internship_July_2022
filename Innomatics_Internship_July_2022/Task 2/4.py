class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        l1 = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i]>nums[j]:
                        count = count + 1
            
            l1.append(count)
            count = 0
        
        return l1