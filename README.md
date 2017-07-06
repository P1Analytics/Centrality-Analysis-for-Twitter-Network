# Seminars in Social Networks and Markets -- Academic Year 2016/17
## Project Request :

### Compute basic statistics (degree distribution) and advanced statistics (clustering coefficient, closeness/betweenness centrality, etc.) for one of the networks of the Stanford Large Network Dataset Collection. 

### If the network is too large, you should use some approximation algorithm (see below for references). Visualize the results using a plotting software such as gnuplot, Gephi or R.

### Implement the fast approximation algorithm of Eppstein and Wang for closeness centrality and use it to compute the closeness centrality of the nodes of a large network.

### Implement one of the fast approximation algorithms of Riondato and Kornaropoulos for betweenness centrality and use it to compute the betweenness centrality of the nodes of a large network.

#### Dataset : http://snap.stanford.edu/data/egonets-Twitter.html

__centrality.pptx__ : related algorithms brief description and results for the measurements 

__AdjacencyList.py__ : create Adjacency List. _Input_: Twitter data files with name format:NodeId.edges. _Output_ : in_degree.csv and out_degree.csv

for the measurments : _Input_ in_degree.csv and out_degree.csv files 

__degree_centrality.py__ : calculate in-degree and out-degree. 

__closeness_centrality.py__ : calculate closeness for the each node in the graph

__betweenness_centrality.py__ : calculate betweenness for each node in the graph 



[1] [Centrality Wikipedia](https://en.wikipedia.org/wiki/Centrality)

[2] [Centrality measures](http://www.dis.uniroma1.it/~bonifaci/semcn/centrality.pdf)

[3] David Eppstein, Joseph Wang. [Fast Approximation of Centrality](http://www.dis.uniroma1.it/~bonifaci/semcn/Eppstein2004.pdf)

[4] Ulrik Brandes. [A Faster Algorithm for Betweenness Centrality](http://www.algo.uni-konstanz.de/publications/b-fabc-01.pdf)

[5] Matteo Riondato, Evgenios M. Kornaropoulos. [Fast Approximation of Betweenness Centrality through Sampling](http://www.dis.uniroma1.it/~bonifaci/semcn/Riondato2014.pdf)
