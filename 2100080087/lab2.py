import numpy as np
n=int(input())
m=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
matrix1=np.array(a).reshape(n,m)
matrix2=np.array(b).reshape(n,m)
matrix2=matrix2.T
print(matrix1)
print(matrix2)
mat=list()
s=[]
for j in range(n):

    for i in range(m):
        s.extend(matrix1[i][j:])
        s.extend(matrix2[i][j:])

        s.remove(max(s))

        mat.append(max(s))

        s.clear()
mat=np.array(mat).reshape(n,m)
print(mat)
