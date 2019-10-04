14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)

9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
            
        if x < 0:
            return False
        
        div = 1
        while x/div >= 10:
            div = div * 10
        while x:
            right = x % 10
            left = x/div
            if left !=right:
                return False
            x = ( x%div ) / 10
            div = div / 100
        return True    
        
        沒解出來
