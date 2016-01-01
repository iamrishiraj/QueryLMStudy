count1=count2=count3=count4=count5=count6=count7=0
for index in range(1,34):
    inputfile="synthetic1_"+str(index)+"_motif.txt"
    file1=open(inputfile,"r")
    line=file1.readline()
    line=line[:-1]
    file1.close()
    words=line.split("\t")
    count1+=float(words[1])
    count2+=float(words[2])
    count3+=float(words[3])
    count4+=float(words[4])
    count5+=float(words[5])
    count6+=float(words[6])
    count7+=float(words[7])

print count1/15,count2/15,count3/15,count4/15,count5/15,count6/15,count7/15
