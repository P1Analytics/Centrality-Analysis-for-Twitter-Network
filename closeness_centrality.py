import ast
import datetime
import random
from collections import defaultdict
import sys
import time
import matplotlib.pyplot as plt

def SSSP(graph,source):
    visited_node = []
    distance = defaultdict(lambda: sys.maxsize)
    distance[source] = 0
    Q = [[source]]
    while Q:
        path = Q.pop(0)
        node = path[-1]
        if node in visited_node:
            continue
        visited_node.append(node)
        for adjacent in graph.get(node, []):
            if adjacent == source:
                continue
            distance[adjacent] = min(distance[adjacent], distance[node] + 1)
            new_path = list(path)
            new_path.append(adjacent)
            Q.append(new_path)
    print(distance.items())
    return (len(distance.values())-1)/sum(distance.values())


def RAID(graph, source, target):
    result_list = []
    visited_node = []
    distance = defaultdict(lambda: sys.maxsize)
    distance[source] = 0
    Q = [[source]]
    while Q:
        if not target:
            return sum(result_list)
        path = Q.pop(0)
        node = path[-1]
        if node in visited_node:
            continue
        visited_node.append(node)
        for adjacent in graph.get(node, []):
            if adjacent == source:
                continue
            distance[adjacent] = min(distance[adjacent], distance[node] + 1)
            if adjacent in target:
                result_list.append(distance[adjacent])
                target.remove(adjacent)
            new_path = list(path)
            new_path.append(adjacent)
            Q.append(new_path)
    return sum(result_list)


if __name__ == "__main__":
    degree_file = "out_degree.csv"
    degree_dict = {}
    with open(degree_file, 'r')as file:
        for line in file:
            degree_dict[int(line.split(":")[0])] = ast.literal_eval(line.split(":")[1])

    out_node_list = list(degree_dict.keys())
    number_nodes = len(out_node_list)
    source = random.choice(list(out_node_list))
    # source = 222563776
    print("from source :", source)

    print("RAND-SSSP")
    sampled_target = []
    sample_k = 40
    print("sample_k", sample_k)
    before = datetime.datetime.now()
    start_time = time.time()
    for i in range(1, sample_k):
        sampled_target.append(random.choice(out_node_list,replace=False))
    sampled_distance = RAID(degree_dict, source, sampled_target)
    final_closeness_centrality = sample_k * (number_nodes - 1) / number_nodes / float(sampled_distance)
    print("average distance ", final_closeness_centrality, "time cost : ", time.time() - start_time)
    print("Running time from ", before, "to", datetime.datetime.now())

    print("Naive-SSSP")
    before = datetime.datetime.now()
    start_time = time.time()
    print("closeness centrality ", (number_nodes - 1) / SSSP(degree_dict, source), "time cost : ",
          time.time() - start_time)
    print("Running time from ", before, "to", datetime.datetime.now())



    # PLOT the result
    # x_ticks = [5, 10, 15, 20, 25, 30, 35, 40]
    # average = [0.2777738150150664, 0.2380918414414855, 0.22726948501232708, 0.2127629221391998, 0.2049151094373441,
    #            0.21897497826005236, 0.2160463005672739, 0.21621313168740305]
    # plt.title('Closeness Approximation for source node 222563776')
    # plt.xlabel("Sample K")
    # plt.axis([5, 45, 0.175, 0.28])
    # plt.plot(x_ticks, average, label='Average Closeness Centrality')
    # plt.axhline(y=0.18625166400514415, color='k', linestyle='--', label='Ground Truth')
    # plt.legend()
    # plt.show()