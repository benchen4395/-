#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:28:00 2019

@author: chenben
"""

# DAG的拓扑排序
graph = {
    "A": ["B","F"],
    "B": ["C","D","F"],
    "C": ["D"],
    "D": ["E","F"],
    "E": ["F"],
    "F": []}


graph2 = {
    "A": {"B":2,"F":9},
    "B": {"C":1,"D":2,"F":6},
    "C": {"D":7},
    "D": {"E":2,"F":3},
    "E": {"F":4},
    "F": {}}

def topsort(G):
    # 创建入队字典
    count = dict((u,0) for u in G)
    
    for u in G:
        for t in G[u]:
            count[t] += 1
    Q = [u for u in G if count[u] == 0]
    res = []
    while Q:
        node = Q.pop()
        res.append(node)
        for i in G[node]:
            count[i] -= 1
            if count[i] == 0:
                Q.append(i)
    return res
print(topsort(graph2))

# DAG最短路径
def dag_sp(W,s,t):
    d = dict((u,float('inf')) for u in W)
    d[s] = 0
    for u in topsort(W):
        if u==t: break
        for i in W[u]:
            d[i] = min(d[i],d[u]+W[u][i])
    return d[t]
print(dag_sp(graph2,'B','F'))
