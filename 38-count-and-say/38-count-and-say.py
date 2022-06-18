class Solution:
    def countAndSay(self, n: int) -> str:
        def count(num):
            ret = ""
            n_str = str(num)
            ptr = 0
            
            while(ptr < len(n_str)):
                count = 1
                _num = n_str[ptr]
                ptr += 1
                while(ptr > 0 and ptr < len(n_str) and n_str[ptr - 1] == n_str[ptr]):
                    count += 1
                    ptr += 1
            
                ret += (str(count) + str(_num))

            return ret
        
        if(n == 1):
            return "1"
        ret = int(count(1))
        for i in range(n - 2):
            ret = int(count(ret))
        
        return(str(ret))