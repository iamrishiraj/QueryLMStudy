import sys

outputfile=open(sys.argv[1]+"_avgshortpath_masterfile.txt","a")
for index in range(1,101):
    filename=sys.argv[1]+"_avg_shrtpath_"+str(index)+"_m1.txt"
    file1=open(filename,"r")
    line=file1.readline()
    line=line[:-1]
    file1.close()
    words=line.split(" ")
    for i in words:
        outputfile.write(str(i)+"\t")
    outputfile.write("\n")

outputfile.close()
