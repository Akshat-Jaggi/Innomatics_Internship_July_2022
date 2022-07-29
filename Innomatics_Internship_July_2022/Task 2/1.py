class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = address.split(".") 
        #Split the input string whenever "." is there and return list of strings
        
        return '[.]'.join(arr) 
        #return a single string where you join all the strins in the list with the connector "[.]"
        
        