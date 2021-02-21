class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        inventory.append(0)
        inventory.sort(reverse = True)

        currWidth = 1
        profit = 0
        def getSum(low, high):
            return high*(high+1)//2 - low*(low+1)//2
        
        for i in range(len(inventory)-1):
            canSell = inventory[i]-inventory[i+1]
            if canSell:
                if currWidth*canSell<=orders:
                    #normal case

                    #calculate profit so far 
                    profit += currWidth * getSum(inventory[i+1], inventory[i])
                    orders-= currWidth * canSell
                    
                else:
                    
                    #divmod case
                    
                    whole, left = divmod(orders, currWidth)
                    profit += currWidth * getSum(inventory[i]-whole, inventory[i])
                    profit += left*(inventory[i]-whole)
                    break
                    
                    
            currWidth+=1
        
        return profit% (10**9 + 7)
