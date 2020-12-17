import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, socks):
    if n < 1 | n > 100:
        return 0
    if not isinstance(socks, list):
        return 0
    for sock in socks:
        if sock < 1 | sock > 100:
            return 0

    sock_map = {}
    for sock in socks:
        if sock in sock_map:
            sock_map[sock] = sock_map.get(sock) + 1
        else:
            sock_map[sock] = 1
    total = 0
    for sock in sock_map:
        total += int(sock_map[sock] / 2)

    return total

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    # n = 9
    # ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    # n = 100
    # ar = "44 55 11 15 4 72 26 91 80 14 43 78 70 75 36 83 78 91 17 17 54 65 60 21 58 98 87 45 75 97 81 18 51 43 84 54 66 10 44 45 23 38 22 44 65 9 78 42 100 94 58 5 11 69 26 20 19 64 64 93 60 96 10 10 39 94 15 4 3 10 1 77 48 74 20 12 83 97 5 82 43 15 86 5 35 63 24 53 27 87 45 38 34 7 48 24 100 14 80 54".split(" ")

    n = 1
    ar = 100

    result = sockMerchant(n, ar)
    print(result)
