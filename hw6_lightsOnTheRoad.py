# coding=UTF-8

__author__ = 'johnqiao'

'''
    We model a road as a numeric range [0, L] on the x axis, where L is the length of the road.
    You are given a set S of coordinates within [0,L], which are places on the road that need light.
    Each light can light up a consecutive range of length K to the right of it.
    That is, if a light is installed at coordinate x, it can light up the range [x, x + K].

    Your task is to find the minimum number of lights required so that all the places in S can get light.

    For example, let L = 10,S = {1,2,3,8,9},K = 2, the answer is 2.
    We can install two lights at x = 1, covering [1, 3] and x = 7, covering [7, 9].
'''


def lights_on_the_road(L, S, K):
    result = []
    need_new_light = True
    k = 0

    for i in range(0, len(S) - 1):
        cur = S[i]
        nex = S[i + 1]
        if need_new_light:
            result.append(cur)
            k = K
            need_new_light = False

        if cur + k < nex:
            need_new_light = True
            # If the last spot is not covered
            if i == len(S) - 2:
                result.append(nex)
        else:
            k -= nex - cur

    print result


if __name__ == '__main__':
    L = (x for x in range(0, 11))
    S = [2, 4, 6, 7, 9]
    K = 4
    lights_on_the_road(L, S, K)

