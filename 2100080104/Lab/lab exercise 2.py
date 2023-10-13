import numpy as np
n=int(input())
m=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
matrix_1=np.array(a).reshape(n,m)
matrix_2=np.array(b).reshape(n,m)
matrix_2=matrix_2.T
print(matrix_1)
print(matrix_2)
mat=list()
s=[]
for j in range(n):

    for i in range(m):
        s.extend(matrix_1[i][j:])
        s.extend(matrix_2[i][j:])
        s.remove(max(s))
        mat.append(max(s))
        s.clear()
mat=np.array(mat).reshape(n,m)
print(mat)
