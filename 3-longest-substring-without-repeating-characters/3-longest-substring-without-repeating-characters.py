class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 255
        _maxlen = 0
        low = 0
        _len = 0
        for high in range(len(s)):
            arr[ord(s[high])] += 1
            _len += 1
            while(arr[ord(s[high])] > 1):
                arr[ord(s[low])] -= 1
                low += 1
                _len -= 1
            _maxlen = max(_maxlen, _len)
            
        return _maxlen