#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
import math
"""有限域"""
def func():
    n = int(input())
    n0 = []
    flag = 1
    z = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if (i % j) == 0:
                flag = 0
                continue
        if flag == 1:
            n0.append(i)
        else:
            flag = 1
    z = int(math.ceil(len(n0)/2))
    print len(n0), sorted(n0)
    print z
    if pow(n0[z], 2) > n:
        for k in range(z):
            for l in range(2, n + 1):
                if pow(n0[k], l) < n:
                    n0.append(pow(n0[k], l))
    print len(n0), sorted(n0)



if __name__ == '__main__':
    func()