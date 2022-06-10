class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ''
        
        for char in s:
            if(char.isalnum()):
                news += char
        
        low, high = 0, len(news) - 1
        
        while(low < high):
            if(news[low] != news[high]):
                return False
            low += 1
            high -= 1
        
        return True