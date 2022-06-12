class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sptr, tptr = len(s) - 1, len(t) - 1
        sjump, tjump = 0, 0
        
        while(sptr >= 0 or tptr >= 0):
            while(sptr >= 0 or sjump == 0):
                if(s[sptr] == '#'):
                    sjump += 1
                elif(sjump > 0):
                    sjump -= 1
                else:
                    break
                sptr -= 1
            while(tptr >= 0):
                if(t[tptr] == '#'):
                    tjump += 1
                elif(tjump > 0):
                    tjump -= 1
                else:
                    break
                tptr -= 1
            
            if(tptr < 0 and sptr < 0):
                return True
            elif((tptr < 0 and sptr >= 0) or (tptr >= 0 and sptr < 0)):
                return False
            elif(t[tptr] != s[sptr]):
                return False
        
            sptr -= 1
            tptr -= 1
        
        return True
            
            
            