def fibo(n):
    if memoization[n]!=-1:
        return memoization[n]

    memoization[n]=fibo(n-1)+fibo(n-2)
    return memoization[n]
    
    
n=10

memoization=[-1 for i in range(n+1)]
memoization[0]=0
memoization[1]=1
fibo(n)
print(memoization)