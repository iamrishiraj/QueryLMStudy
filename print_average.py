counterfile=open("Counter_for_bigram_select.txt","r")
sum1=0
counter=0
for i in counterfile:
    i=i.strip("\n")
    counter+=1
    sum1+=int(i)

average=float(sum1)/counter

print average
