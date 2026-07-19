class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):

            if "0" in str(i):
                continue

            valid = True

            for num in str(i):

                if i % int(num) != 0:
                    valid = False
                    break

            if valid:
                ans.append(i)

        return ans