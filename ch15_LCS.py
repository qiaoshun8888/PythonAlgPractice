# coding=UTF-8

__author__ = 'johnqiao'

'''
    In the longest-common-subsequence problem,
    we are given two sequences X D hx1; x2; :::; xmi and Y D hy1; y2; :::; yni and
     wish to find a maximum- length common subsequence of X and Y .
'''


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, longest_x = 0, 0

    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    longest_x = x
            else:
                m[x][y] = 0

    return s1[longest_x - longest: longest_x]


if __name__ == '__main__':
    s1 = 'thisisatest'
    s2 = 'testing123testing'

    print list(xrange(10))[::2]
    print list(xrange(0, 10, 2))[::-1]

    print longest_common_substring(s1, s2)