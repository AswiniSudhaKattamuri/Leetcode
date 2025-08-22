class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        curr = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)   
            elif ch == "[":
                numStack.append(num)
                strStack.append(curr)
                num = 0
                curr = ""
            elif ch == "]":
                repeat = numStack.pop()
                prevStr = strStack.pop()
                curr = prevStr + curr * repeat
            else: 
                curr += ch

        return curr
