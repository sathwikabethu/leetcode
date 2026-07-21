class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            count=0
            while(num>0):
                count+=num%10
                num//=10
            num=count
        return num
       



        