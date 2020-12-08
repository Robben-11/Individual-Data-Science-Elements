## Question: Given an unsorted integer list: cost (intger >= 1), an intger: money
## Return the index of two elements that summed together equal to the integr
## The question has only unique solution 
## cost can have differnet positions with the same cost 

def whatFlavors(cost, money):
    
    dic = {}
    for i in range(len(cost)): 
        if cost[i] < money: 
            
            ## Handling repeated caost
            if cost[i] in dic: 
                pass
            ## 
            
            else:
                dic[cost[i]] = i 

        if money - cost[i] in dic and i!= dic[money - cost[i]]: ## Used the constant time operation character of dictionary
            
            print (dic[money - cost[i]]+1 , i+1)
            return 
          
## Medium - 35
## 100% success  
## O(n)
