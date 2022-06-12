class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sptr, tptr = len(s) - 1, len(t) - 1
        sjump, tjump = 0, 0
        while(sptr >= 0 or tptr >= 0):
            while(sptr >= 0):
                if(s[sptr] == '#'):
                    sjump += 1
                    sptr -= 1
                else:
                    break
            while(tptr >= 0):
                if(t[tptr] == '#'):
                    tjump += 1
                    tptr -= 1
                else:
                    break
            while(sjump > 0):
                sptr -= 1
                if(sptr < 0):
                    break
                if(s[sptr] == '#'):
                    sjump += 1
                else:
                    sjump -= 1
            while(tjump > 0):
                tptr -= 1
                if(tptr < 0):
                    break
                if(t[tptr] == '#'):
                    tjump += 1
                else:
                    tjump -= 1
        
            if(not (sptr >= 0) ^ (tptr < 0)):
                return False
            if(sptr >= 0 and tptr >= 0 and s[sptr] != t[tptr]):
                #print(sptr, tptr, s[sptr], t[tptr])
                return False
            
            sptr -= 1
            tptr -= 1
            
        return True