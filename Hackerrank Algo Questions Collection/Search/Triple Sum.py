def triplets(a, b, c):

    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    
    counter_a = 0  
    counter_c = 0
    result = 0 
    for i in range(len(b)): 

        while (counter_a <= len(a)-1): 

            if (a[counter_a] <= b[i]): 

                 counter_a += 1 
            
            else: 
                break 
            
        while (counter_c <= len(c)-1): 

            if (c[counter_c] <= b[i]): 

                 counter_c += 1 
            else: 
                break 

        result += counter_a * counter_c 


    return result 
