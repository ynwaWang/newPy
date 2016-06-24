#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sqrt
import pydelicious

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You,Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You,Me and Dupree': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You,Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You,Me and Dupree': 2.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You,Me and Dupree': 2.0
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You,Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}


# 返回一个有关person1与person2的基于距离的相似度评价
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 如果两者没有共同之处，则返回0
    if len(si) == 0:
        return 0

    sum_of_squares = sum(
        [pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]]
    )
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    n = len(si)

    if n == 0: return 1

    # 对所有偏好求和
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    # 求平方和
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])

    # 求乘积和
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

    # 计算皮尔逊评价值
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0
    r = num / den
    return r


"""
相似度高的好友推荐
"""
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


"""
推测出自己对影片的评价 = 相似度高的（没看过的）片子推荐
每个人的趣味差异很大，对片子的评分自然会有很大的差距，所谓加权，就是相似度高的人会提供更多输出
"""
def getRecommendations(prefs, person, n=5, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue
        for item in prefs[other]:
            # 只对自己还未曾看过的影片进行评价的部分
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # 平均评价 - 归一化处理
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings[0:n]


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # 将物品和人对换
            result[item][person] = prefs[person][item]
    return result


movies = transformPrefs(critics)

if __name__ == '__main__':
    # print topMatches(critics, 'Toby', 3)
    # print getRecommendations(critics, 'Toby', 3)
    # print topMatches(movies, 'Superman Returns', 3)
    # print getRecommendations(movies, 'Just My Luck', 3)
    print pydelicious.get_popular(tag='programming')
