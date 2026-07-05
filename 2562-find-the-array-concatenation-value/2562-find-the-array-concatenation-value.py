class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value=0
        left=0
        right=len(nums)-1
        while left<right:
            concat_value+=int(str(nums[left])+str(nums[right]))
            left+=1
            right-=1
        if left==right:
            concat_value+=nums[left]
            
        return concat_value
        