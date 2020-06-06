'''
You are given an array A of N integers and three integers B, C, and D.
You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.
'''
class Solution:
    def solve(self, A, B, C, D):
        left_max = [0]*len(A)
        right_max = [0]*len(A)
        _max = 0 
        left_max[0] = B*A[0]
        right_max[-1] = D*A[-1]
        
        for i in range(1, len(left_max)):
            left_max[i] = max(left_max[i-1], B*A[i])
        
        for j in range(len(A)-2, -1, -1):
            right_max[j] = max(right_max[j+1], D*A[j])
        
        for i in range(0, len(A)):
            _max = max(_max, left_max[i] + right_max[i] + C*A[i])
        
        return _max