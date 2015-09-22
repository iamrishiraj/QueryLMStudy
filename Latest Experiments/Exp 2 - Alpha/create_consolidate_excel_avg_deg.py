outfile=open("average_list.csv","w")
for index in range(0,20):
    avdeg_file_name="avgdeg_synthetic4_random_1m_001_stemmed_alpha_"+str(index*0.1)+".txt"
    avdeg_list=open(avdeg_file_name,"r")
    lines=avdeg_list.readlines()
    tempstr=""
    for i in lines:
        line_trim=i[:-1]
        value=line_trim.split(":")
        tempstr=tempstr+value[1]+","
        
    outfile.write(tempstr)
    outfile.write("\n")
outfile.close()