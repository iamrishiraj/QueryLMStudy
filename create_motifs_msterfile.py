import sys

outputfile=open(sys.argv[1]+"_motif_masterfile.txt","a")
for index in range(1,101):
    filename=sys.argv[1]+"_"+str(index)+"_0.1m_motifs.txt"
    filename1=sys.argv[1]+"_random_0.1m_"+str(index)+"_lcc.txt"
    file1=open(filename,"r")
    file2=open(filename1,"r")
    line=file1.readline()
    line=line[:-1]
    tolines=file2.readlines()
    tolines=tolines[2:]
    file1.close()
    file2.close()
    noedges=len(tolines)
    words=line.split(" ")
    for i in words:
        outputfile.write(str(i)+"\t")
    outputfile.write(str(noedges))
    outputfile.write("\n")

outputfile.close()
