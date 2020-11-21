class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        # Переводим каждый символ в число
        for i, j in enumerate(s):
            if j == 'I': s[i] = 1
            elif j == 'V': s[i] = 5
            elif j == 'X': s[i] = 10
            elif j == 'L': s[i] = 50
            elif j == 'C': s[i] = 100
            elif j == 'D': s[i] = 500
            elif j == 'M': s[i] = 1000
        result = 0
        last = 0
        for i in s: result += i-last*2 if last < i else i; last = i
        return result


print(Solution().romanToInt(input()))
