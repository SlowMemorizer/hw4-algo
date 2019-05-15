#-*- coding:utf-8 -*-
import sys
from copy import deepcopy

INF = sys.maxsize

graph = [ 
    [0, 2, 5, 1, INF, INF], 
    [2, 0, 3, 2, INF, INF], 
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]

node_num = len(graph)
visited = [ False for i in range(node_num) ]
cost = [ INF for i in range(node_num) ]


def FindMinCostNode():
    crnt_min_cost = sys.maxsize
    min_node_idx = 0

    for i in range(node_num):
        if cost[i] < crnt_min_cost and not visited[i]:
            crnt_min_cost = cost[i]
            min_node_idx = i 
    return min_node_idx



def Dijkstra(begin):
    for i in range(node_num):
        cost[i] = graph[begin][i]
    visited[begin] = True         # 시작노드는 방문처리

    for i in range(node_num-2):   # 시작노드, 마지막노드 제외(마지막엔 마지막 노드를 제외하곤 모두 방문함)
        crnt_min = FindMinCostNode()
        visited[crnt_min] = True
        for j in range(node_num):
            new_cost = cost[crnt_min] + graph[crnt_min][j]
            if not visited[j] and new_cost < cost[j]:
                cost[j] = new_cost
    

def Floyd():
    g = deepcopy(graph)

    for k in range(node_num):
        for i in range(node_num):
            for j in range(node_num):
                new_cost = g[i][k] + g[k][j]
                g[i][j] = min(g[i][j], new_cost)
    return g



if __name__ == '__main__':    
    for i in range(node_num):
        Dijkstra(i)
        print('{} -> {}'.format(i, cost))
        visited = [ False for i in range(node_num) ]

    for cost  in Floyd():
        print(cost)