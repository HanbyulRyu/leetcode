class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         coins = [186,419,83,408]
#         amount = 6249
        
        if amount == 0:
            return 0

        t = [2**31-1]*(amount+1)
        t[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                t[i] = min(t[i], t[i-coin]+1)
                
        if t[amount] == (2**31-1):
            return -1
        
        # print(t)
        return t[amount]
        
#         coins.sort(reverse=True)    
#         result = 0
      
#         for i in range(len(coins)):
#             q, m = divmod(amount, coins[i])
#             if q > 0:
#                 result += q
#             amount = m 
            
#         if amount > 0:
#             return -1
            
#         return result
        