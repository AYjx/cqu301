#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

"""回文数"""
def func():
    n = int(input())
    count = 0
    for i in range(n+1):
        s = str(bin(i))[2:]
        s2 = s[::-1]
        if s == s2:
            count += 1
        print s, s2
    print count

if __name__ == '__main__':
    func()