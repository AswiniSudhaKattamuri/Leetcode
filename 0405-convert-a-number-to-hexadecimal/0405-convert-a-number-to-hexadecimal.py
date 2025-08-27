class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"
        
        hex_characters = "0123456789abcdef"
        result = []
        
        
        if num < 0:
            num += 2**32  
        
        while num > 0:
            remainder = num % 16
            result.append(hex_characters[remainder])
            num //= 16  
        
        result.reverse()
        
        return ''.join(result)

