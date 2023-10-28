import numpy as np
n = int(input())
m = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
m1 = np.array(a).reshape(n, m)
m2 = np.array(b).reshape(n, m)
#print(m1)
#print(m2)
matrix = list()
s = []
for i in range(n):
    for j in range(m):
        for k in range(m):
            s.append(max(m1[i][k], m2[k][j]))

        matrix.append(min(s))
        s.clear()

matrix = np.array(matrix).reshape(n, m)
print(matrix)
