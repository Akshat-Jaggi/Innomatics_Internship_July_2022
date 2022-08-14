class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict1 = {}
        li = []
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        
        for key,value in dict1.items():
            if value == 1:
                li.append(key)
        
        return li
                