class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lst=[]
        max_value=max(nums)
        min_value=min(nums)
        for i in range(min_value,max_value+1):
            if i not in nums:
                lst.append(i)
        return sorted(lst)


        