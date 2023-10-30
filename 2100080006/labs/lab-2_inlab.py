import numpy as np
n=int(input())
m=int(input())
a=list(map(float,input().split()))
b=list(map(float,input().split()))
matrix1=np.array(a).reshape(n,m)
matrix2=np.array(b).reshape(n,m)
print(matrix1)
print(matrix2)
mat=list()
s=[]
for i in range(n):
    for j in range(m):
        for k in range(m):
            s.append(max(matrix1[i][k],matrix2[k][j]))
        mat.append(min(s))
        s.clear()
mat=np.array(mat).reshape(n,m)
print(mat)


