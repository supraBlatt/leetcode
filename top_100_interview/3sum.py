from ast import List
import itertools
class Solution:

    # we want to return all triples n[i], n[j], n[k] where i != j != k that sum to 0
    # naive O(n^3) approach - check all triplets
    # naive O(n^2) approach is using reduction. fix one number and use 2-sum 
    # - one version of 2-sum is with sorting, and the other is with a hashtable
    # another one I'm aware of uses decision trees but idk how to implement that

    # helper function!! returns the doubles that sum to target, with no redundencies
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for n in nums:
            if (target-n) in seen:


        for i in range(len(nums)-1):
                    


        return result
    
    # big fanni name!!!!
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # no need to check the last 2 
        for i in range(len(nums)-2):
            # to prevent repetitions we'll only use elements following it..
            # there's still the issue of order. so - 1,2,3 and 1,3,2 would be the same
            # but counted as different sequences
            target = nums[i]
            two_sum = self.twoSum(self, nums[i+1:], -target)
            result += map(lambda x: x + target, two_sum)

        return result
