def harm(n):
    if n==1:
        return 1/n
    else:
        return 1/n + harm(n-1)

if __name__=="__main__":
    print(harm(2))
    print(harm(100))
