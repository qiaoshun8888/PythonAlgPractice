__author__ = 'johnqiao'

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