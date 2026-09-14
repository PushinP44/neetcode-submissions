class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create set from list
        numSet = set(nums)

        longest = 0

        #find starting point
        for n in nums:
            if n-1 not in numSet:
                length = 0
                while n in numSet:
                    length+=1
                    n+=1
                longest = max(length,longest)
        return longest