import random

for index in range(1,101):
    if index<10:
        filename="artificial_random_1m_00"+str(index)+"_stemd.txt"
    elif index<100:
        filename="artificial_random_1m_0"+str(index)+"_stemd.txt"
    else:
        filename="artificial_random_1m_"+str(index)+"_stemd.txt"

    file1=open(filename,"r")
    lines=file1.readlines()
    file1.close()

    query=random.sample(lines,100000)

    outputname="sample_logs/artificial_random_stemd_0.1m_"+str(index)+".txt"
    outputfile=open(outputname,"w")
    for i in query:
        outputfile.write(str(i))
    outputfile.close()
