import ast
import datetime
import queue
import random
from collections import defaultdict
import numpy as np


def Brandes_Betweenness(graph, start,Cb):
    Q = queue.Queue()  # FIFO
    S = []  # list as stack : LIFO
    Pred = defaultdict(lambda: [])
    distance = defaultdict(lambda:-1)
    distance[start] = 0
    sigma = defaultdict(lambda: 0)
    sigma[start] = 1
    Q.put(start)

    while not Q.empty():
        v = Q.get()
        if v in S:  # prevent a loop back to the visited node and go into circles
            continue
        S.append(v)
        for w in graph.get(v, []):
            if distance[w] < 0:
                Q.put(w)
                distance[w] = distance[v] + 1
            if distance[w] == distance[v] + 1:
                sigma[w] += sigma[v]
                Pred[w].append(v)

    delta = defaultdict(lambda: 0)
    # Cb = defaultdict(lambda: 0)  # betweenness centrality for each node
    while S:
        w = S.pop()
        for v in Pred[w]:
            delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
        if w != start:
            Cb[w] += delta[w]
    return Cb


def Matteo_Betweenness(graph,source,target,r,Cb):
    Q = queue.Queue()  # FIFO
    S = []  # list as stack : LIFO
    Pred = defaultdict(lambda: [])
    distance = defaultdict(lambda:-1)
    distance[source] = 0
    sigma = defaultdict(lambda: 0) # number of paths through this node
    sigma[source] = 1
    Q.put(source)

    while not Q.empty():
        v = Q.get()
        if v in S:  # stop back to the visited node
            continue
        if target == v:
            break
        S.append(v)
        for w in graph.get(v, []):
            if distance[w] < 0:
                Q.put(w)
                distance[w] = distance[v] + 1
            if distance[w] == distance[v] + 1:
                sigma[w] += sigma[v]
                Pred[w].append(v)

    if len(Pred[target])>0:
        trace_back = queue.Queue()
        trace_back.put(np.random.choice(Pred[target]))
        while not trace_back.empty():
            v = trace_back.get()
            if source == v:
                break
            Cb[v] += 1/r
            if len(Pred[v])>0:
                trace_back.put(np.random.choice(Pred[v]))
    # print(Cb.items())


def find_r(graph,source):
    Q = queue.Queue()  # FIFO
    S = []  # list as stack : LIFO
    distance = defaultdict(lambda:-1)
    distance[source] = 0
    sigma = defaultdict(lambda: 0) # number of paths through this node
    sigma[source] = 1
    Q.put(source)

    while not Q.empty():
        v = Q.get()
        if v in S:  # stop back to the visited node
            continue
        S.append(v)
        for w in graph.get(v, []):
            if distance[w] < 0:
                Q.put(w)
                distance[w] = distance[v] + 1
            if distance[w] == distance[v] + 1:
                sigma[w] += sigma[v]
    return sorted(list(sigma.values()))[-2:]


if __name__ == "__main__":

    degree_file = "out_degree.csv"
    degree_dict = {}
    with open(degree_file, 'r')as file:
        for line in file:
            degree_dict[int(line.split(":")[0])] = ast.literal_eval(line.split(":")[1])
    source_list = list(degree_dict.keys())

    # fast algorithm
    Cb = defaultdict(lambda: 0)
    for start in source_list:
        begin = datetime.datetime.now()
        Cb = Brandes_Betweenness(degree_dict, start,Cb)
        print("start from node :", start,"start:", begin, "end:", datetime.datetime.now())
        # break


    # faster algorithm
    # find r
    start = np.random.choice(source_list)
    print("start to find r")
    max_1, max_2 = find_r(degree_dict, start)
    VD_G=max_1+max_2
    print("VD_G is",VD_G)
    epsilon = 0.05
    c = 0.5
    delta = 0.1
    r = (c / np.math.pow(epsilon, 2)) * (np.math.floor(np.math.log(VD_G - 2, 2)) + np.math.log(1 / delta))
    r = np.math.ceil(r)
    print("r is ",r)

    # BETWEENNESS Sampling
    degree_file = "in_degree.csv"
    target_list = []
    with open(degree_file, 'r')as file:
        for line in file:
            target_list.append(int(line.split(":")[0]))

    Cb = defaultdict(lambda:0)
    begin = datetime.datetime.now()
    for i in range(1,r):
        start = np.random.choice(source_list, replace=False)
        stop = np.random.choice(target_list, replace=False)
        print("start node is:", start, "stop node is ", stop)
        Matteo_Betweenness(degree_dict,start,stop,r,Cb)
        # break

    print("start time :", begin, "end time:", datetime.datetime.now())
    top_k = 10
    print("the top", top_k, "nodes are:", sorted(Cb.items(), key=lambda x: -x[1])[:top_k])


