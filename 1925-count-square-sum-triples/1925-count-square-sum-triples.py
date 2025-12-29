class Solution:
    def countTriples(self, n: int) -> int:
        import math
        count=0
        for a in range(1,n):
            for b in range(1,n):
                s=a*a+b*b
                c=int(math.sqrt(s))
                if c*c==s and c<=n:
                    count+=1
        return count
