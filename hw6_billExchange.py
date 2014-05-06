# coding=UTF-8

__author__ = 'johnqiao'

'''
    Let S be a set of integers representing bill values.
    For example, for US dollars we have Sus = {1, 5, 10, 20, 50, 100}.
    For a given amount k, your task is to find the minimum number of bills that can compose k dollars.

    1. What is the optimal solution for 379 dollars on Sus?
    2. Give a greedy algorithm that solves the task on Sus.
    3. Show that the greedy algorithm doesn’t work if the set S is arbitrarily chosen, by providing a counterexample.
'''


bills = [1, 5, 10, 20, 50, 100]
result = [0]


def bill_exchange_recursively(k, bi):
    if k >= bills[bi]:
        k -= bills[bi]
        result[0] += 1
        if k == 0:
            print bills
            while len(result) < len(bills):
                result.insert(0, 0)
            print result
        else:
            bill_exchange_recursively(k, bi)
    else:
        bi -= 1
        result.insert(0, 0)
        bill_exchange_recursively(k, bi)


def bill_exchange_iteratively(k):
    bi = len(bills) - 1
    while k:
        if k >= bills[bi]:
            k -= bills[bi]
            result[0] += 1
            if k == 0:
                break
        else:
            bi -= 1
            result.insert(0, 0)
    print bills
    while len(result) < len(bills):
        result.insert(0, 0)
    print result


if __name__ == '__main__':
    bill_exchange_recursively(379, len(bills) - 1)
    result = [0]
    bill_exchange_iteratively(379)