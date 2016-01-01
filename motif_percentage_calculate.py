for index in range(1,2):
    inputstr="artificialf_random_1m_"+str(index)+"_avgdeg_cluster.txt"
    file1=open(inputstr,"r")
    lines=file1.readlines()
    file1.close()
    words=lines[1].split(":")
    nodes=words[1][:-1]
    nodes=int(nodes)
    Nc3= (nodes*(nodes-1)*(nodes-2))/6
    Nc4= (nodes*(nodes-1)*(nodes-2)*(nodes-3))/24

    inputstr1="synthetic2_"+str(index)+"_motif.txt"
    file2=open(inputstr1,"r")
    for line in file2:
        line=line.strip("\n")
        line=line.strip("\t")
        mvalue=line.split("\t")

    print mvalue
    print Nc3,Nc4
