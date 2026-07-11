class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        carry = 0
        ans = []

        n = max(len(num1), len(num2))

        for i in range(n):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0

            total = digit1 + digit2 + carry

            ans.append(str(total % 10))
            carry = total // 10

        if carry:
            ans.append(str(carry))

        return "".join(ans[::-1])
        