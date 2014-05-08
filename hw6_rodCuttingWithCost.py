# coding=UTF-8

__author__ = 'johnqiao'

'''
    Given an initial rod of integer length m and a table that 
    gives the values of rods with integer lengths from 1 to m, 
    you can solve the rod cutting problem 
    (computing the maximum value you can get after cutting) using dynamic programming. 
    Now, suppose cutting the rod intro- duces a non-negative cost 
    (you lose value if you cut at that position). 
    The cost is different if you cut at different positions. 
    That is, you are given another table that tells you the cost of cutting 
    at each integer position x respectively (1 ≤ x ≤ m − 1). 
    The goal is still to get the maximum value after cutting. 
    How would you modify your dynamic programming algorithm to solve the new rod cutting problem?

    For example, suppose m = 4, the values of rods with length 1,2,3,4 are 0,10,1,0 
    respectively and the cutting costs at position 1, 2, 3 are 0, 20, 0 respectively. 
    Then instead of cutting the rod into two rods of length 2 
    (get value 2×10 but cost 20 for cutting, so you get nothing at last), 
    you shall cut at x = 1 or x = 3 (get value 0 + 1 = 1 but cost 0 for cutting, so you get 1 at last).
'''

def rod_cutting(prices, cost, n):
    len_p = len(prices)
    dp = [0 for i in xrange(len_p)]
    result = [0 for i in xrange(len_p)]

    rod_cutting_iteratively(prices, cost, n, dp, result)

    k = n - 1 # convert length to index
    cuts = []
    while k > 0:
        i = result[k]
        cuts.append((k - i + 1, i, prices[i - 1], cost[k - i]))
        k -= i
    
    print 'dp:\t\t', dp
    print 'result:\t', result
    print '\n'
     
    return dp[n - 1], cuts


def rod_cutting_iteratively(prices, cost, n, dp, result):
    for i in xrange(n):
        q = float('-inf')
        for j in xrange(i + 1):
            c = cost[i - j - 1] if j != i else 0
            v = prices[j] + dp[i - j - 1] - c
            # print 'v: ', v, ' cost: ', c, ' i: ', i + 1, 'j: ', j + 1
            if q < v:
                q = v
                result[i] = j + 1
        dp[i] = q


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    c = [1, 1, 2, 0,  2,  7,  5,  2,  1, 0]
    
    # p = [0, 10, 1, 0] 
    # c = [1, 20, 1]

    value, cuts = rod_cutting(p, c, 10)

    print 'total value: ', value
    print 'cuts(cut point / length / value / cost): ', cuts
