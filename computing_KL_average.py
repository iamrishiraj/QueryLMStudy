file1=open("KL_Distribution for Segment-Synthetic3.txt","r")
sum=0
for i in file1:
    i=i.strip("\n")
    words=i.split("\t")
    sum+=float(words[1])

average=sum/100
print average
