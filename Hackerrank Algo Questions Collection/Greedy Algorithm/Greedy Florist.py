

# get the sorted cost of flowers in descending order 
# pirchase will start from the most expensive flower, recorder the number of purchase for each person 
# multiple the cost with new times of the purchases when every person has purchased for one round 
# Rotate through rounds
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
