filename=open("createstemdfile.sh","w")
for i in range(1,101):
    if i<10:
        outputstr="./PorterStemmer.out synthetic7_random_1m_00"+str(i)+".txt > synthetic7_random_1m_00"+str(i)+"_stemmed.txt"
    elif i<100:
        outputstr="./PorterStemmer.out synthetic7_random_1m_0"+str(i)+".txt > synthetic7_random_1m_0"+str(i)+"_stemmed.txt"
    else :
        outputstr="./PorterStemmer.out synthetic7_random_1m_"+str(i)+".txt > synthetic7_random_1m_"+str(i)+"_stemmed.txt"
    filename.write(str(outputstr)+"\n")
filename.close()


