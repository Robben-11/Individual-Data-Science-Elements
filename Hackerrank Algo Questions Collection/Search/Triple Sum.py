##IMPORTANT: There is another version of this question using binary search, in which there are some errors, but the idea has also proven under O(nlogn) 

## Step1: Remove the duplicates, we are only talking about combinations of triplets, having repeated numbers in b does not add up. Having repeated elements in a and c 
## also does not make sense as well since for a given b, having another number repeated in any list does not add a new combination to the existing profile. 

## Step 2: Sort, this allow us to place the counter at the position when each single element in b has gone through the search. So the search does not come back to
# its original place. 

## Time complexity O(nlogn)

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
