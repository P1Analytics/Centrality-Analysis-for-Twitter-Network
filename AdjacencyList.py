import csv
from os import listdir
from os.path import isfile, join
# from the http://snap.stanford.edu/data/egonets-Twitter.html


def map_out_degree(line, file_name):
    list_pairs = []
    line = line.split()
    if "#" in line[1]:
        return list_pairs
    list_pairs.append((file_name, int(line[0])))
    list_pairs.append((file_name, int(line[1])))
    list_pairs.append((int(line[0]), int(line[1])))
    return list_pairs


def map_in_degree(line, file_name):
    list_pairs = []
    line = line.split()
    if "#" in line[1]:
        return list_pairs
    list_pairs.append((int(line[0]), file_name))
    list_pairs.append((int(line[1]), file_name))
    list_pairs.append((int(line[1]), int(line[0])))
    return list_pairs


def reduce_degree(degree, degree_file):
    degree_dict = {}
    for degree_i in degree:
        if degree_i[0] in degree_dict:
            degree_dict[degree_i[0]].append(degree_i[1])
        else:
            degree_dict[degree_i[0]] = [degree_i[1]]

    for key, value in degree_dict.items():
        value_no_dup = list(set(value))
        degree_dict[key] = value_no_dup
    print("start to write into degree file " + degree_file+ " and the total length for it is "+ str(len(degree_dict.keys())) +" lines" )
    with open(degree_file, 'w')as file:
        writer = csv.writer(file,delimiter=':')
        for i in degree_dict.items():
            writer.writerow(i)


if __name__ == "__main__":
    path = "/Users/nanazhu/Documents/LosAlamos/twitter"
    # path = "/Users/nanazhu/Documents/LosAlamos/edges"

    edges_files = [f for f in listdir(path) if isfile(join(path, f))]
    out_degree = []
    in_degree = []

    for file_name in edges_files:
        path_file = join(path, file_name)
        if file_name == ".DS_Store":
            continue
        file_name = int(file_name.split(".")[0])
        with open(path_file) as f:
            for line in f:
                if map_out_degree(line, file_name) == [] or map_in_degree(line, file_name) == []:
                    break
                out_degree += map_out_degree(line, file_name)
                in_degree += map_in_degree(line, file_name)

    reduce_degree(out_degree, "out_degree.csv")
    reduce_degree(in_degree, "in_degree.csv")
