filename=open("synthetic7_random_clustercoef.txt","w")
for index in range(1,101):
    prop="synthetic7_random_1m_"+str(index)+"_avgdeg_cluster.txt"
    propfile=open(prop,"r")
    lines=propfile.readlines()
    propfile.close()
    cluster=lines[-1]
    avgdeg=lines[-2]
    avgdeg=lines[-2]
    edges=lines[0]
    nodes=lines[1]
    deg=avgdeg.split(":")
    edg=edges.split(":")
    nod=nodes.split(":")
    if deg[1][-1]=="\n":
        deg[1]=deg[1][:-1]
    if nod[1][-1]=="\n":
        nod[1]=nod[1][:-1]
    if edg[1][-1]=="\n":
        edg[1]=edg[1][:-1]
    words=cluster.split(":")
    if words[1][-1]=="\n":
        words[1]=words[1][:-1]
    filename.write(str(index))  
    filename.write("\t") 
    filename.write(str(words[1]))
    filename.write("\t")
    filename.write(str(deg[1]))
    filename.write("\t")
    filename.write(str(nod[1]))
    filename.write("\t")
    filename.write(str(edg[1]))
    filename.write("\n")
filename.close()
