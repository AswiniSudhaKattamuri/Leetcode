class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newstr = ''
        max_length = 0   
        for char in s:
            if char in newstr:
                newstr = newstr[newstr.index(char) + 1:]
            newstr += char
            max_length = max(max_length, len(newstr))
        return max_length
