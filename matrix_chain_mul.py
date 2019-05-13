# -*- coding:utf-8 -*-
# python3
import sys    # sys.maxsize


# Dynamic Programming
def MatrixChain(d, n):
    # 0행과 0열은 사용하지 않습니다. 
    m = [ [0 for x in range(n)] for y in range(n) ] 

    for chain in range(1, n):
        for begin in range(1, n-chain):
            end = begin + chain   
            m[begin][end] = sys.maxsize
            for k in range(begin, end):     
                new_cost = m[begin][k] + m[k+1][end] + (d[begin-1]*d[k]*d[end])
                m[begin][end] = min(m[begin][end], new_cost)      

    return m[1][-1]



# Brute Force
def MatrixChain_BruteForce(d, begin, end):
    if begin == end: return 0
    min_num = sys.maxsize

    for k in range(begin, end):
        new_cost = (
              MatrixChain_BruteForce(d, begin, k)     
            + MatrixChain_BruteForce(d, k+1, end)   
            + (d[begin-1] * d[k] * d[end]) 
        )
        min_num = min(min_num, new_cost)

    return min_num
        

# Main
if __name__ == '__main__':
    d = [ x for x in range(1, 17) ]
    
    min_num_dp = MatrixChain(d, len(d))
    print('Dynamic Programming: %d' % min_num_dp)

    min_num = MatrixChain_BruteForce(d, 1, len(d)-1)
    print('Brute Force: %d' % min_num)
