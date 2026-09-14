class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            res.append(0)

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        
        for i in range(len(nums)):
            res[len(nums)-i-1]*=postfix
            postfix*=nums[len(nums)-i-1]
        
        return res
        


