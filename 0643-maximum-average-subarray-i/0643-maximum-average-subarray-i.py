class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # n=len(nums)-k+1
        # lst=[]
        # for i in range(n):
        #     total=0
        #     for j in range(i,k+i):
        #         total+=nums[j]
        #     avg=total/k
        #     lst.append(avg)
        #     max_val=max(lst)
        # return max_val
        
        

        
        # lst=[]
        # n=len(nums)-k+1
        # for i in range(n):
        #     sum1=sum(nums[i:k+i])
        #     avg=sum1/k
        #     lst.append(avg)
            
        # return max(lst)


        win_sum=sum(nums[:k])
        max_sum=win_sum

        for i in range(k,len(nums)):
            win_sum=win_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,win_sum)
        return max_sum/k

