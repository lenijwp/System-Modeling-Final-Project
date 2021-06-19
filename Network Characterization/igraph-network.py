import csv
from igraph import Graph as IGraph

txt_file_list = [
    './email-EuAll.txt/Email-EuAll.txt',
    './web-Stanford.txt/web-Stanford.txt'
]

def get_node_and_edge_from_txt(file_name):
    data_list = []
    for line in open(file_name, "r"):
        data_list.append(line)
    data_list = data_list[4:]

    nodes = []
    edges = []
    for i in data_list:
        str_list = i.split('\t')
        node1 = str_list[0]
        node2 = str_list[1].split('\n')[0]

        edge_pair = []
        edge_pair.append(node1)
        edge_pair.append(node2)
        edge = tuple(edge_pair)

        nodes.append(node1)
        edges.append(edge)
    nodes = list(set(nodes))
    print('Num of nodes in data: ', len(nodes))
    print('Num of edges in data: ', len(edges))

    return nodes, edges

for i in txt_file_list:
    nodes, edges = get_node_and_edge_from_txt(i)
    g = IGraph.TupleList(
        edges,
        directed=False,
        vertex_name_attr='name',
        edge_attrs=None,
        weights=False
    )
    # print("网络直径： ", g.diameter())


    # g_degree = g.degree()  # 度
    # print(g_degree[:10])
    g_cluster = g.transitivity_undirected() # 聚类系数
    print(g_cluster)
    # g_betweenness = g.betweenness() # 介数中心性
    # print(g_betweenness[:10])
    # g_closeness = g.closeness()  # 紧密中心性
    # print(g_closeness[:10])
    # g_eigenvector = g.eigenvector_centrality()  # 特征中心性
    # print(g_eigenvector[:10])
    # g_harmonic_centrality = g.harmonic_centrality() # 调和中心性
    # print(g_harmonic_centrality[:10])

    #g_clustering_coefficient = g.clustering_coefficient()

    #print(g.clusters())




