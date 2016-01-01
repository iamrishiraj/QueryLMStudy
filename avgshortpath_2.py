import networkx as nx

templist=[]
filename=open("real_random_1m_50_lcc.txt","r")
lines=filename.readlines()
lines=lines[2:]
for i in lines:
    words=i.split("\t\t\t")
    templist.append((words[0],words[1][:-1]))
filename.close()

total=0
counter=1
counter1=1
g=nx.Graph()
g.add_edges_from(templist)
for i in g.nodes():
	for j in g.nodes():
        	if i!=j:
            		x=nx.shortest_path_length(g,i,j)
            		total+=x
            		avgpath=float(total)/counter
            		counter+=1
        	else:
            		pass	
	
	fileout=open("average_short_path_50.txt","a")
      	fileout.write(str(avgpath))
      	fileout.write("\n")
       	fileout.close()
    	
	if i!=j: 
		percent=float(counter1)/len(g.nodes())
        	filepercent=open("percentagecompleted.txt","w")
        	filepercent.write(str(percent))
        	counter1+=1
        	filepercent.close()
	else:
		pass
