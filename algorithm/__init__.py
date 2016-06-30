#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    算法汇总
"""

"""
    最大公约数，欧几里得算法=辗转相除法
"""
def gcd(a, b):
    print a, b
    return a if b == 0 else gcd(b, a % b)


"""
    倒水问题 : x*A + y*B = C
             或者 x*A % B = C
    http://www.acmerblog.com/pour-water-problem-5615.html
"""
def water(cup1, cup2, goal_volume):
    pass

"""
    守擂算法，可扩展至多擂主
"""
def arena(participants):
    n_times = 0
    for part in participants:
        if n_times == 0:
            candidate = part
            n_times += 1
        elif candidate == part:
            n_times += 1
        else:
            n_times -= 1
    return candidate


if __name__ == '__main__':
    print gcd(48, 30)
