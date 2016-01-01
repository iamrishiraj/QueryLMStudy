tempdict={}
filename=open("AnjanaQueries.txt","r")
lines=filename.readlines()
filename.close()
noofquery=len(lines)
for i in lines:
    i=i[:-1]
    words=i.split(" ")
    l = len(words)
    if l == 2:
        continue 
    trigram=words[0]+" "+words[1]+" "+words[2]
    try:
        tempdict[trigram]+=1
    except KeyError:
        tempdict[trigram]=1

fileoutput=open("Trigram_comes_1st_prob.txt","w")
fileoutput.write("Trigram\t\tP(N)\t\tCumulative\n\n")
previous=0
for i in tempdict.keys():
    fileoutput.write(str(i))
    fileoutput.write("\t\t")
    value=float(tempdict[i])/noofquery
    fileoutput.write(str(value))
    fileoutput.write("\t\t")
    previous+=value
    fileoutput.write(str(previous))
    fileoutput.write("\n")

fileoutput.close()

