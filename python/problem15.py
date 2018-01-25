n=21
m = []
for i in range (0,n):
    arr=[]
    for i in range(0,n):
        arr.append(0)
    m.append(arr)

for i in range(0,n):
    m[i][n-1]=1
    m[n-1][i]=1
for i in xrange(n-2,-1,-1):
    m[i][i]=m[i+1][i]*2
    for j in xrange(i-1,-1,-1):
        m[i][j]=m[i+1][j]+m[i][j+1]


print m[0][0]