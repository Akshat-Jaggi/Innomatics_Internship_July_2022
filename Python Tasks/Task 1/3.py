class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l1 = []
        
        for i in range(len(candies)):
            sum1 = candies[i] + extraCandies
            if sum1 >= max(candies):
                l1.append(True)
            else:
                l1.append(False)
            sum1 = 0
            
        return l1
        