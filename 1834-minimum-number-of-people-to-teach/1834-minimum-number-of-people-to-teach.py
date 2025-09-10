class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
     
        m = len(languages)
        
        langs = [set(l) for l in languages]
        
       
        bad_users = set()
        for u, v in friendships:
            if langs[u-1].isdisjoint(langs[v-1]):
                bad_users.add(u-1)
                bad_users.add(v-1)
        
        if not bad_users:
            return 0
        
        ans = float('inf')
      
        for L in range(1, n+1):
            count = sum(1 for user in bad_users if L not in langs[user])
            ans = min(ans, count)
        
        return ans
