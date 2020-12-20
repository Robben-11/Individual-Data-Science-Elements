def minimumAbsoluteDifference(arr):

    arr = sorted(arr) 
    result = 2 * 10**9
    i = 0
    while i <= len(arr)-2: 

        if abs(arr[i] - arr[i+1]) <= result: 

            result = abs(arr[i] - arr[i+1])

        i += 1 

    return result 
