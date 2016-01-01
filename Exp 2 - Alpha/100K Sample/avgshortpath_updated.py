import networkx as nx
import sys

for index in range(0,20):
    templist=[]
    filename=open("lcc_synthetic4_random_0.1m_001_stemmed_alpha_"+str(index*0.1)+".txt","r")
    lines=filename.readlines()
    lines=lines[2:]
    for i in lines:
        words=i.split("\t\t\t")
        templist.append((words[0],words[1][:-1]))
    filename.close()
        
    g=nx.Graph()
    g.add_edges_from(templist)
    x=nx.average_shortest_path_length(g)
    
    fileout=open("avgshortpath_synthetic4_random_0.1m_001_stemmed_alpha_"+str(index*0.1)+".txt","w")
    fileout.write("Average shortest path length:")
    fileout.write(str(x))
    fileout.close()
