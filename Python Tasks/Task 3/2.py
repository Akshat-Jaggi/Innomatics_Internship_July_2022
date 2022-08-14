class Solution:
    def numTeams(self, rating: List[int]) -> int:
        L = len(rating)
        result = 0
        
        for j in range(1,L-1):
            x,lo_L,hi_L,lo_R,hi_R = rating[j],0,0,0,0
            for i in range(j):
                if rating[i] < x:
                    lo_L = lo_L + 1
                elif rating[i]>x:
                    hi_L = hi_L + 1
            for k in range(j+1,L):
                if rating[k] < x:
                    lo_R = lo_R + 1
                elif rating[k]>x:
                    hi_R = hi_R + 1   
            result = result + hi_R*lo_L + hi_L*lo_R
        
        return result