class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value -> index
        for i,n in enumerate(nums):
            diff = target - n
            #check if any diff is in hashmap before
            if diff in prevMap: return [prevMap[diff],i]
            #add to hashmap
            prevMap[n]=i