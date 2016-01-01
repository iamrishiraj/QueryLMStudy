tempdict={}
filename=open("AnjanaQueries.txt","r")
lines=filename.readlines()
filename.close()
length=len(lines)
for i in lines:
    i=i[:-1]
    words=i.split(" ")
    numberofwords=len(words) 
    for j in range(0,numberofwords-2):
        string=words[j]+" "+words[j+1]+" "+words[j+2]
        try:
            tempdict[string]+=1
        except KeyError:
            tempdict[string]=1

fileoutput=open("Consecutive_Trigram_Probability.txt","w")
fileoutput.write("Words\t\tP(N)\n\n")
for i in tempdict.keys():
    fileoutput.write(str(i))
    fileoutput.write("\t\t")
    value=float(tempdict[i])/length
    fileoutput.write(str(value))
    fileoutput.write("\n")

fileoutput.close()


