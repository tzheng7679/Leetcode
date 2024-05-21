class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        carry = 0

        # Sign extension if one is shorter than the other (and why can't arr1 and arr2 be of the same length you doofuses?)
        if len(arr1) > len(arr2):
            arr2 = [0] * (len(arr1) - len(arr2)) + arr2
        
        elif len(arr2) > len(arr1):
            arr1 = [0] * (len(arr2) - len(arr1)) + arr1
        
        # Extension on both to prevent overflow
        arr1 = [0, 0] + arr1
        arr2 = [0, 0] + arr2

        n = len(arr1)
        out = [0] * (n)

        carry = 0
        for i in range(n - 1, 1, -1):
            add = arr1[i] + arr2[i] + carry
            
            out[i] += add % 2
            carry = -(add // 2)
        
        out[1] += carry

        for i in range(n - 1, -1, -1):
            if out[i] == -1:
                out[i] += 2
                out[i - 1] += 1
            
            if out[i] >= 2:
                out[i] = out[i] % 2

                out[i - 1] -= 1

        # cut off leading zeros
        try:
            chop = out.index(1)
            return out[chop:]
        except:
            return out[:1]
        
print(Solution.addNegabinary(Solution, [1], [1]))