class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kmap={} #number->count
        for key in nums:
            if key not in kmap: kmap[key] = 0
            kmap[key]+=1
        
        res = []

        while k != 0:
            top = max(kmap, key = kmap.get)
            res.append(top)
            del kmap[top]
            k-=1
        
        return res