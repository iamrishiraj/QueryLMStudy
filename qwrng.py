#This program can be used for both segment and word queries.We just have to change the name of the reading files
import pickle

temp={}
f=open("wordnodelist.txt","r")
lines=f.readlines()
lines=lines[2:len(lines)]
for i in lines:
    words=i.split("\t\t")
    temp[words[0]]=words[2][:-1]
f.close()

f2=open("qwung.txt","r")
f3=open("qwrng.txt","w") #to create a restricted graph
f3.write("Node 1\t\t\t")
f3.write("Node 2\t\t\t")
f3.write("P(12)\n\n")
rline=f2.readlines()
rline=rline[2:len(rline)]
for i in rline:
    nodes=i.split("\t\t\t")
    value=float(temp[nodes[0]])*float(temp[nodes[1]])
    if float(nodes[2])>value:
        f3.write(str(nodes[0]))
        f3.write("\t\t\t")
        f3.write(str(nodes[1]))
        f3.write("\t\t\t")
        f3.write(str(nodes[2]))
    else:
        pass

f2.close()
f3.close()
