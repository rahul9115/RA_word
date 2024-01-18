a=[1,2,3,4]
'''
000
001
010
011
100
101
110
111
'''
l=[]
c=[]


for i in range(1,2**len(a)):
    s=[]
    for j in range(len(a)):
        if i&(1<<j):
            s.append(a[j])
    l.append(s)
print(l)


