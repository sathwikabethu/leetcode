class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=abs(x)
            sign=-1
        else:
            sign=1
        rev=0
        while x>0:
            temp=x
            temp%=10
            rev=rev*10+temp
            x//=10
        result=sign*rev
        if -2**31<=result<=2**31 -1:
            return result
        else:
            return 0
