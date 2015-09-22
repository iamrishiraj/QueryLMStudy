import networkx as nx
import sys

for index in range(1,20):
    g=nx.Graph()
    edge=[]
    redgelist="rnl_synthetic4_random_1m_001_stemmed_updated_alpha_"+str(index*0.1)+".txt"
    edgefile=open(redgelist,"r")
    lines=edgefile.readlines()
    final=lines[2:]
    for i in final:
        finalline=i[:-1]
        nodes=finalline.split("\t\t\t")
        edge.append((nodes[0],nodes[1]))
    edgefile.close()
    g.add_edges_from(edge)
    h=list(nx.connected_component_subgraphs(g))[0]
    lcc="lcc_synthetic4_random_1m_001_stemmed_updated_alpha_"+str(index*0.1)+".txt"
    lccfile=open(lcc,"w")
    lccfile.write("Node 1\t\t\tNode 2\n\n")
    for u,v in h.edges():
        lccfile.write(str(u))
        lccfile.write("\t\t\t")
        lccfile.write(str(v))
        lccfile.write("\n")
    lccfile.close()
    prop="avgdeg_synthetic4_random_1m_001_stemmed_updated_alpha_"+str(index*0.1)+".txt"
    propertfile=open(prop,"w")
    propertfile.write("Number of edges:")
    propertfile.write(str(h.size()))
    propertfile.write("\nNumber of nodes:")
    propertfile.write(str(len(h.nodes())))
    avgdeg=float(h.size())*2/len(h.nodes())
    propertfile.write("\nAverage degree:")
    propertfile.write(str(avgdeg))
    cluster=nx.average_clustering(g)
    propertfile.write("\nAverage Clustering Coeffident:")
    propertfile.write(str(cluster))
    propertfile.close()
