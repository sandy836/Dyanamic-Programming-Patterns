"""
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is 
maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.
"""
def adjacent(self, A):
    if len(A[0]) == 1:
        return max(A[0][0], A[1][0])
        
    pre_processed = []
    for i in range(0, len(A[0])):
        pre_processed.append(max(A[0][i], A[1][i]))
    pre_processed[1] = max(pre_processed[1], pre_processed[0])
    
    for i in range(2, len(pre_processed)):
        pre_processed[i] = max(pre_processed[i]+pre_processed[i-2], pre_processed[i-1])
    return pre_processed[-1]