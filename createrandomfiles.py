#create 100 files with random 1 million queries
import random

try:
    file=open("AnjanaQueries.txt","r")
    lines=file.readlines()
    file.close()
except IOError :
    print "The filename doesnt exist.Please check"

for i in range(1,101):
    if i<10:
        filename="real_random_1m_00"+str(i)+".txt"
    elif (i>=10 and i <100):
        filename="real_random_1m_0"+str(i)+".txt"
    else:
        filename="real_random_1m_"+str(i)+".txt"
    output=open(filename,"w")
    temp=random.sample(lines,1000000)
    for j in temp:
        output.write(str(j))
    output.close()
