# coding=UTF-8

__author__ = 'johnqiao'


def rod_cutting(prices, n):
    dp = [0 for i in range(len(prices))]
    result = [0 for i in range(len(prices))]

    dp[0] = prices[0]
    result[0] = 1

    # rod_cutting_recursively(prices, n - 1, dp, result)
    rod_cutting_iteratively(prices, n - 1, dp, result)

    return dp, result


def rod_cutting_recursively(prices, n, dp, result):
    if dp[n] > 0:
        return dp[n]

    q = 0
    if n == 0:
        q = 0
    elif q == 0:
        for i in range(0, n + 1):
            v = prices[i] + rod_cutting_recursively(prices, n - i - 1, dp, result)
            if q < v:
                q = v
                result[n] = i + 1

    dp[n] = q

    return q


def rod_cutting_iteratively(prices, n, dp, result):
    for i in range(0, n + 1):
        q = 0
        for j in range(0, i + 1):
            v = prices[j] + dp[i - j - 1]
            if q < v:
                q = v
                result[i] = j + 1
        dp[i] = q


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    r, s = rod_cutting(p, 10)

    print 'r: ', r
    print 's: ', s