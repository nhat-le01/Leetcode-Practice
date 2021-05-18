'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start, end = 0, 0
        result = 1
        table = set()
        while end < len(s):
            while end < len(s) and s[end] not in table:
                table.add(s[end])
                end += 1
            #There is a repeated character
            result = max(result, end - start)
            #shrinking until there is no repeated character
            while end < len(s) and s[end] in table:
                table.remove(s[start])
                start += 1
        return result
            
            
            
        
