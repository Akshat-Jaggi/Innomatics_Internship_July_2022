class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        stack = []

        for n in arr:
            count = bin(n)[2:].count("1") 
            # "2:" to remove "0b" from the start and count to count number of 1s in binary
            stack.append([count, n])
        
        stack.sort()
        arr = [num for c, num in stack]
        return arr