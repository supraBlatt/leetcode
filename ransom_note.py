

from collections import Counter

class Solution:
    # initial sketch..
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       # use counters 
       return not Counter(ransomNote) - Counter(magazine) 
