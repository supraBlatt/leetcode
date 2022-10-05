from ast import List
import itertools

class Solution:

    # initial sketch. thanks python discord for helping with syntax.. 
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        
        # why even
        to_letters = {
                '2': ['a', 'b', 'c'], 
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }

        # honestly don't think i'll try going for something better..
        # but I believe this is also doable with list comprehension 
        return map(''.join, itertools.product(*map(to_letters.get, digits)))
