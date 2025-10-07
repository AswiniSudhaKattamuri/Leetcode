class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from bisect import bisect_right
        n = len(rains)
        ans = [-1] * n
        full = set()
        dry_days = []
        last_rain = {}

        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    idx = bisect_right(dry_days, last_rain[lake])
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  
                    dry_days.pop(idx)
                full.add(lake)
                last_rain[lake] = i
                ans[i] = -1
            else:
                dry_days.append(i)
                ans[i] = 1  
        return ans

        