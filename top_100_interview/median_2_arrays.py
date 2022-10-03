from ast import List
import heapq
from re import I

class Solution:

    # one naive way is to merge the arrays and then find the median index. 
    # o(n + m) time and space, i believe
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge lists - lmao i'm cheating no way I'm implementing merge sort merge
        m = list(heapq.merge(nums1, nums2))
        l = len(m)
        return m[l//2] if l%2 else (m[l//2] + m[l//2 - 1])/2

    # apparently this could be done in logarithmic time. challenge for tomorrow i guess
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass