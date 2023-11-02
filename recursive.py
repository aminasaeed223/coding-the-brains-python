# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     result = n*factorial (n-1)
#     return result 
#     # pass 
# def determinent(n):
#     n = len(A)
#     if n==1:
#         return A[0][0]
#     else:
#         sign = 1
#         det = 0
#         for j in range(n):
#             sub_matrix=[]
#             for i in range(1, n):
#                 sub_row = []
#                 for k in range(n):
#                     if k != j:
#                         sub_row.append(A[i][k])
#                     sub_matrix.append(sub_row)
#             element = sign *A[0][j]* determinent(sub_matrix)
#             det +=sign *A[0][j]* determinent(sub_matrix)
            
#             sign = sign * (-1)
#         return det
import numpy as np
def numpy_determinent(matrix):
    np.linalg.det(matrix)

            
                
# factorial(5)

if __name__ =="__main__":
    # print(factorial(9))
    A = [[1,2,3,4],
         [3,4,5,6],
         [7,8,9,10],
         [1,2,3,4]]
print(numpy_determinent(A))
