import sys

tempdict={}
filename=open(sys.argv[1],"r")
lines=filename.readlines()
filename.close()
counter=0
for i in lines:
    i=i[:-1]
    words=i.split(" ")
    numberofwords=len(words) 
    for j in range(0,numberofwords-2):
        try:
            strname=words[j]+" "+words[j+1]+" "+words[j+2]
            tempdict[strname]+=1
        except KeyError:
            tempdict[strname]=1
    counter+=numberofwords-2

fileoutput=open(sys.argv[2],"w")
fileoutput.write("Trigram\t\tP(N)\n\n")
for i in tempdict.keys():
    fileoutput.write(str(i))
    fileoutput.write("\t\t")
    value=float(tempdict[i])/counter
    fileoutput.write(str(value))
    fileoutput.write("\n")

fileoutput.close()

