
def getMinimumCost(k, c):
    
    c = sorted(c, reverse=True)
    
    if k >= len(c): 
        return sum(c)

    else: 
        
        result = 0
        no_purchase = [1]*k
        
        for i in range(len(c)): 
            
            if i+1 > k: 
                
                no_purchase[i%k] += 1 
                result += no_purchase[i%k] * c[i]
                
            else: 
                
                result += c[i]
                
        return result 
