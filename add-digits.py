class Solution:
    def addDigits(self, num: int) -> int:
        s = 0

        while num > 0:
            s += num % 10
            num = num // 10
        
        if s >= 10:
            return Solution.addDigits(self, s)
        
        return s


print(Solution.addDigits(Solution, 38))