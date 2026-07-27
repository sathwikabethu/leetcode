class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        s=""
        for i in range(len(x)-1,-1,-1):
            s=s+x[i]
        if s==x:
            return True
        else:
            return False        