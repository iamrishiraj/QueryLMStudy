inputfile=open("real_random_1m_1_lcc.txt","r")
lines=inputfile.readlines()
inputfile.close()

templist=[]
lines=lines[2:]
for i in lines:
    i=i[:-1]
    words=i.split("\t\t\t")
    if int(words[1])<int(words[0]):
        templist.append((int(words[1]),int(words[0])))
    else:
        templist.append((int(words[0]),int(words[1])))

templist.sort()

outputfile=open("real_adjacency_list_for_1.txt","w")
flag=0
previous=0
for (u,v) in templist:
    if flag==0:
        outputfile.write(str(u))
        outputfile.write(" ")
        outputfile.write(str(v))
        previous=u
        flag=1
    elif (flag==1 and u==previous):
        outputfile.write(" ")
        outputfile.write(str(v))
    elif (flag==1 and u!=previous):
        outputfile.write("\n")
        outputfile.write(str(u))
        outputfile.write(" ")
        outputfile.write(str(v))
        previous=u


outputfile.close()
