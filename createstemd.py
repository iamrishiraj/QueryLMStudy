filename=open("create_stemd_file.bat","w")
for index in range(1,101):
    if index<10:
        strname="PorterStemmer.exe artificial_random_1m_00"+str(index)+".txt > artificial_random_stemd_1m_00"+str(index)+".txt"
    elif (index>=10 and index<100):
        strname="PorterStemmer.exe artificial_random_1m_0"+str(index)+".txt > artificial_random_stemd_1m_0"+str(index)+".txt"
    else:
        strname="PorterStemmer.exe artificial_random_1m_"+str(index)+".txt > artificial_random_stemd_1m_"+str(index)+".txt"
    filename.write(str(strname))
    filename.write("\n")
filename.close()
