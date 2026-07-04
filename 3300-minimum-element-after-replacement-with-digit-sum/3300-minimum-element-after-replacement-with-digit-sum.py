class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            sum=0
            while i>0:
                temp=i
                temp%=10
                sum+=temp
                i//=10
            l.append(sum)
        return min(l)



        