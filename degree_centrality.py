import ast
from collections import Counter
import matplotlib.pyplot as plt

if __name__ == "__main__":
    twitter_nodes = 81306
    degree_file = "out_degree.csv"
    # degree_file = "in_degree.csv"

    max_degree = 0
    degree_list = []
    with open(degree_file, 'r')as file:
        for line in file:
            size = len(ast.literal_eval(line.split(":")[1]))
            degree_list.append(size)

    max_degree = max(degree_list)

    print("max degree is ", max_degree)
    print("total degree list is Cd(v) =  ", degree_list)

    sum = 0
    for i in degree_list:
        sum += max_degree - i
    degree_centrality = sum / (twitter_nodes - 1) * (twitter_nodes - 2)
    print("degree_centrality(G)", degree_centrality)

    plt.xlabel('degree x ')
    plt.ylabel('frequence of degree(x)')
    plt.title('Out-Degree Distribution')
    # plt.title('In-Degree Distribution')

    counts = Counter(degree_list)
    plt.bar(range(len(counts)), counts.values())
    plt.show()
