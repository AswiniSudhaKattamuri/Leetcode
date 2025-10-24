class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            s = str(x)
            for d in set(s):
                if s.count(d) != int(d):
                    return False
            return True

        num = n + 1
        while True:
            if is_balanced(num):
                return num
            num += 1
