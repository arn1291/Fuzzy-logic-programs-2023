import numpy as np
num_rows = int(input())
num_cols = int(input())
input_matrix1 = list(map(int, input().split()))
input_matrix2 = list(map(int, input().split()))
matrix1 = np.array(input_matrix1).reshape(num_rows, num_cols)
matrix2 = np.array(input_matrix2).reshape(num_rows, num_cols)
matrix2_transposed = matrix2.T

print("Matrix 1:")
print(matrix1)
print("Transposed Matrix 2:")
print(matrix2_transposed)

result_matrix = list()
temp_list = []
for j in range(num_rows):
    for i in range(num_cols):
        temp_list.extend(matrix1[i][j:])
        temp_list.extend(matrix2_transposed[i][j:])
        temp_list.remove(max(temp_list))
        result_matrix.append(max(temp_list))
        temp_list.clear()
result_matrix = np.array(result_matrix).reshape(num_rows, num_cols)
print("Resultant Matrix:")
print(result_matrix)
