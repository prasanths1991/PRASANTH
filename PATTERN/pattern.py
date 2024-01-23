def pattern(n):
    for i in range(1,n+1):
        print("*"*i,end="\n")

    for i in range(1,n):
        t = n - i
        print(" "*i,"*"*t)

pattern(4)
