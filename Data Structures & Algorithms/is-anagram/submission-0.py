class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #same length
        if len(s) != len(t): return False

        res_s = {}
        res_t = {}

        for i in range(len(s)):
            if s[i] not in res_s: res_s[s[i]]=1
            else: res_s[s[i]]+= 1

            if t[i] not in res_t: res_t[t[i]]=1
            else: res_t[t[i]]+= 1
        
        for key in res_s:
            if res_s.get(key) != res_t.get(key): return False
        
        return True
        