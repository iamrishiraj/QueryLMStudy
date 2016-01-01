import pickle
import sys

for index in range(1,2):
    temp={}
    value=0.0
    nodecreate="nodelist_synthetic4_random_1m_001_stemmed.txt"#+sys.argv[1]
    f=open(nodecreate,"r")
    lines=f.readlines()
    lines=lines[2:len(lines)]
    for i in lines:
        words=i.split("\t\t")
        temp[words[0]]=words[2][:-1]
    f.close()


    for index in range(1,20):
        edgelist="unl_synthetic4_random_1m_001_stemmed.txt"#+sys.argv[1]
        f2=open(edgelist,"r")
        redgelist="rnl_synthetic4_random_1m_001_stemmed_alpha_"+str(index*0.1)+".txt"#+sys.argv[1]
        f3=open(redgelist,"w")
        f3.write("Node 1\t\t\t")
        f3.write("Node 2\t\t\t")
        f3.write("P(12)\n\n")
        rline=f2.readlines()
        rline=rline[2:len(rline)]
        for i in rline:
            nodes=i.split("\t\t\t")
            value=float(temp[nodes[0]])*float(temp[nodes[1]])
            if pow(float(nodes[2]),index*0.1)>value:
                f3.write(str(nodes[0]))
                f3.write("\t\t\t")
                f3.write(str(nodes[1]))
                f3.write("\t\t\t")
                f3.write(str(nodes[2]))
            else:
                pass

        f2.close()
        f3.close()
