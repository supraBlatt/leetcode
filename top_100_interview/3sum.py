from ast import List
import itertools
class Solution:

    # we want to return all triples n[i], n[j], n[k] where i != j != k that sum to 0
    # naive O(n^3) approach - check all triplets
    # naive O(n^2) approach is using reduction. fix one number and use 2-sum 
    # - one version of 2-sum is with sorting, and the other is with a hashtable
    # another one I'm aware of uses decision trees but idk how to implement that

    # helper function!! returns all couples that sum to target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}



        return result
    
    # big fanni name!!!!
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)-2):
            # to prevent repetitions we'll only use elements following it..
            two_sum = self.twoSum(self, nums[i+1:], -nums[i])
            result += map(lambda x: x + nums[i], two_sum)

        return result
