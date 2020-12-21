# use li_to get a sorted list of the cost of important contests. sorted with descending order from the largets cost 
# use l_ui to extract list of costs of unimportnat contests. usorted. 

# Take the required summation of and subtraction specfiied by the question
# Approximate Worsts case complexity: O(nlog(n)+4n) !!! Can be reduced further here.

def luckBalance(k, contests):
    
    l_i = [contests[i][0] for i in range(len(contests)) if contests[i][1] == 1]
    l_i = sorted(l_i, reverse=True)

    l_ui = [contests[i][0] for i in range(len(contests)) if contests[i][1] == 0]

    return sum(l_i[:k]) + sum(l_ui) - sum(l_i[k:])
    
