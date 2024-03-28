#!/bin/python3

import math
import os
import random
import re
import sys

class Solution:
    isSolutionExists = True
    errorMessage = ""


    def cholesky_decomposition(matrix):
        n = len(matrix)
        L = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    L[i][j] = (matrix[i][i] - s) ** 0.5
                elif L[j][j] != 0.0: 
                    L[i][j] = (1.0 / L[j][j] * (matrix[i][j] - s))
                else:
                    raise ValueError("Zero diagonal encountered, Cholesky decomposition cannot proceed.")
        
        return L
    

    def forward_substitution(L, b):
        n = len(b)
        y = [0.0] * n
        
        for i in range(n):
            y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
            
        return y
    

    def backward_substitution(LT, y):
        n = len(y)
        x = [0.0] * n
        
        for i in reversed(range(n)):
            x[i] = (y[i] - sum(LT[i][j] * x[j] for j in range(i+1, n))) / LT[i][i]
        
        return x
    

    def solveByCholeskyDecomposition(n, matrix):
        try:
            L = Solution.cholesky_decomposition(matrix)
        except ValueError as e:
            Solution.isSolutionExists = False
            Solution.errorMessage = str(e)
            return
        
        b = [row[-1] for row in matrix]
        y = Solution.forward_substitution(L, b)
        LT = [[L[j][i] for j in range(n)] for i in range(n)]
        x = Solution.backward_substitution(LT, y)
        
        result = x + y
        return result

if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n + 1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    result = Solution.solveByCholeskyDecomposition(n, matrix)
    if Solution.isSolutionExists:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Solution.errorMessage}")
    print("")
