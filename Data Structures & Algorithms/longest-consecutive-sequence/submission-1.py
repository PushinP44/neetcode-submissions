class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create set from list
        numSet = set(nums)

        longest = 0

        for n in nums:
            #find starting point
            if n-1 not in numSet:
                length = 0
                #find end point
                while n in numSet:
                    length+=1
                    n+=1
                longest = max(length,longest)
        return longest