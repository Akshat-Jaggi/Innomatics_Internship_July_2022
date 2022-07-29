class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1 = 0
        product1 = 1
        
        while(n!=0):
            sum1 = sum1 + int(n%10)
            product1 = product1 * int(n%10)
            n = int(n/10)
        
        diff = product1 - sum1
        return diff