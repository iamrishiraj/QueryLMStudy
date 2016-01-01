import networkx as nx
import sys

for index in range(1,2):
    templist=[]
    name=sys.argv[1]+"_random_1m_"+str(index)+"_lcc.txt"
    filename=open(name,"r")
    lines=filename.readlines()
    lines=lines[2:]
    for i in lines:
        words=i.split("\t\t\t")
        templist.append((words[0],words[1][:-1]))
    filename.close()
        
    g=nx.Graph()
    g.add_edges_from(templist)
    x=nx.average_shortest_path_length(g)
    out=sys.argv[1]+"_avg_shrtpath_"+str(index)+"_m1.txt"
    fileout=open(out,"w")
    fileout.write("Average shortest path length:")
    fileout.write(str(x))
    fileout.close()
