class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + num
        
        dp = [0] * (max(nums) + 2)
        dp[1] = dic.get(1, 0)
        dp[2] = max(dp[1], dic.get(2, 0))
        
        for i in range(3, len(dp)):
            dp[i] = max(dp[i - 2] + dic.get(i, 0), dp[i - 1])
        
        return dp[-1]