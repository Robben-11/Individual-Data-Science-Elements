

def luckBalance(k, contests):
    
    l_i = [contests[i][0] for i in range(len(contests)) if contests[i][1] == 1]
    l_i = sorted(l_i, reverse=True)

    l_ui = [contests[i][0] for i in range(len(contests)) if contests[i][1] == 0]

    return sum(l_i[:k]) + sum(l_ui) - sum(l_i[k:])
    
