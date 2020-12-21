# we sort the array first
# then max(arr') = the last element, and the min(arr') = the first element 
# We calculate the unfairness 
# We only need to iterate in a progressive way, since we are looking for the minimum possible fairness
# Worst case complexity O(nlog(n))

def maxMin(k, arr):
    
    arr = sorted(arr)
    result = 10**9
    for i in range(len(arr)-k+1): 
        
        temp = arr[i+k-1] - arr[i]
        
        if temp < result: 
            
            result = temp 
            
    return result
