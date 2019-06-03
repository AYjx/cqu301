#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

"""一的个数"""
def func():
    s = [int(x) for x in raw_input().split()]
    n = pow(2, s[0]) + pow(2, s[1]) - pow(2, s[2])
    n2 = str(bin(n))
    count = 0
    for i in range(len(n2)):
        if n2[i] == '1':
            count += 1
        else:
            continue
    print n2, len(n2), count


if __name__ == '__main__':
    func()