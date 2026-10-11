class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        groups={}
        for ch,count in freq.items():
            groups.setdefault(count,[]).append(ch)     
        res=max(groups, key=lambda count:(len(groups[count]),count))
        return ''.join(groups[res])   