def FibTab(n):
    tb=[0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[1-2])
    return tb[n-1]