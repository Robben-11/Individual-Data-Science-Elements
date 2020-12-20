

# Question asks for the minimum absolute difference in an unsorted list
# Sorted the list in an ascending order and turn the question into finding the difference between adjacent elements 
# Worst case complexity: O(nlogn + n) 

def minimumAbsoluteDifference(arr):

    arr = sorted(arr) 
    result = 2 * 10**9
    i = 0
    while i <= len(arr)-2: 

        if abs(arr[i] - arr[i+1]) <= result: 

            result = abs(arr[i] - arr[i+1])

        i += 1 

    return result 
