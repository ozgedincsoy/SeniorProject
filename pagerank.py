import networkx as nx
import pickle

D=nx.DiGraph()

dic = pickle.load(open("graph.pickle", "rb"))
dic2= pickle.load(open("filename.pickle", "rb"))

link_list = []

for key in dic:
    first_node = key
    for value in dic[key]:
        second_node = value[0]
        weight = value[1]
        link_list.append((first_node, second_node, weight))
        break

D.add_weighted_edges_from(link_list)

ranks = nx.pagerank(D)

sort = sorted(ranks.items(), key=lambda kv: kv[1], reverse=True)
print(sort[:10])
