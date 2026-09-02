class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append((nums[i],i))
        arr.sort()
        left=0
        right=len(arr)-1
        
        while left<right:
            if arr[left][0]+arr[right][0]==target:
                return [arr[left][1],arr[right][1]]
            elif arr[left][0]+arr[right][0]>target:
                right-=1
            elif arr[left][0]+arr[right][0]<target:
                left+=1

            
        
        