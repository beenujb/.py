x=5
y=5
ans = 0
if x >= 0:
    while ans*ans < x:
        ans = ans + 1
    if ans*ans != x:  
        print ("yes")
    else:
        print ("no")
