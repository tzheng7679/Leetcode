def intToRoman(num: int) -> str:
    s = ""

    numerals = {5000 : "Dummy",
                1000 : "M", 
                500 : "D", 
                100 : "C", 
                50 : "L", 
                10 : "X", 
                5 : "V", 
                1 : "I"}
    bases = numerals.keys

    digits = [0] * 4
    for i in range(3, -1, -1):
        digits[i] = num // (10 ** i)
        
        if digits[i] == 4:
            s += numerals[10 ** i] + numerals[5 * 10 ** i]
        
        elif digits[i] == 9:
            s += numerals[10 ** i] + numerals[10 ** (i + 1)]

        else:
            s += (digits[i] // 5) * numerals[5 * 10 ** i] + (digits[i] - 5 * (digits[i] // 5)) * numerals[10 ** i]

        num = num % (10 ** i)
    
    return s

print(intToRoman(3749))