class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        
        for i in range(n):
            nums.append(start + 2*i)
            
        xor_result = nums[0]
        
        for i in range(1,len(nums)):
            xor_result =  xor_result ^ nums[i]
        
        return xor_result