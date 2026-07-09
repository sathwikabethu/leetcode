class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''result=""
        for i in digits:
            result+=str(i)
        result=int(result)+1
        result_list=[]
        for i in str(result):
            result_list.append(int(i))
        return result_list '''

        '''result=""
        for i in digits:
            result+=str(i)
        result=int(result)+1
        result_list=[]
        while result>0:
            temp=result
            temp%=10
            result_list.append(temp)
            result//=10
        #return result_list.reverse() if we directly return reversed list it returns none
        result_list.reverse()
        return result_list'''
        '''s=0
        for i in digits:
            s=s*10+i
        s+=1
        result=[]
        for i in str(s):
            result.append(int(i))
        return result'''


        '''for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits'''

        num = int("".join(map(str, digits))) + 1

        return list(map(int, str(num)))

        
        