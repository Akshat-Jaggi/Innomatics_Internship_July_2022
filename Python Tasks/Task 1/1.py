class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l1 = []
        sum1 = 0
        
        for i in range(len(nums)):
            for j in range(i+1):
                sum1 = nums[j] + sum1
            l1.append(sum1)
            sum1 = 0
            
        return l1