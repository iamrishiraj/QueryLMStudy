#Remove stopwords from the file

import sys

for index in range(1,2):
    counter=1
    stopdict={}
    stopfile=open("stopwords.txt","r")
    stoplines=stopfile.readlines()
    stopfile.close()
    
    for index in range(0,len(stoplines)):
        stoplines[index]=stoplines[index][:-1]
        stopdict[stoplines[index]]="Yes"
    
    stemfile=open("synthetic4_random_1m_001_stemmed.txt","r")
    stemlines=stemfile.readlines()
    stemfile.close()
    
    stemfile_up=open("synthetic4_random_1m_001_stemmed_updated.txt","w")
    
    for index in range(0,len(stemlines)):
        stemlines[index]=stemlines[index][:-1]
        
    for temp in stemlines:
        linewords=temp.split(" ")
        strdata=""
        for i in range(0,len(linewords)):
            if linewords[i] not in stopdict.keys():
                strdata=strdata+linewords[i]+" "
                          
        strdata=strdata.strip()
            
        if len(strdata)!=0:
            stemfile_up.write(strdata)
            stemfile_up.write("\n")
        
        print str(counter) + " Records Updated"
        counter=counter+1
    stemfile_up.close()