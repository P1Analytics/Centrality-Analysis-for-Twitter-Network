Seminars in Social Networks and Markets -- Academic Year 2016/17
Project Request :

Compute basic statistics (degree distribution) and advanced statistics (clustering coefficient, closeness/betweenness centrality, etc.) for one of the networks of the Stanford Large Network Dataset Collection. 

If the network is too large, you should use some approximation algorithm (see below for references). Visualize the results using a plotting software such as gnuplot, Gephi or R.

Dataset : http://snap.stanford.edu/data/egonets-Twitter.html

AdjacencyList.py : create Adjacency List. Input: Twitter data files with name format:NodeId.edges. Output : in_degree.csv and out_degree.csv

degree_centrality.py : calculate in-degree and out-degree from in_degree.csv and out_degree.csv files 

closeness_centrality.py : calculate closeness for the echo node in the graph

betweenness_centrality.py : calculate betweenness for each node in the graph 

centrality.pptx : algorithms and results
