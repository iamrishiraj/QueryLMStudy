import random

inputfile=open("synthetic4_random_1m_001_stemmed_updated.txt","r")
lines=inputfile.readlines()
inputfile.close()
total_records=len(lines)
max_words=0
for i in lines:
    i=i[:-1]
    words=i.split(" ")
    len_words=len(words)
    if len_words>max_words:
        max_words=len_words

for i in lines:
    i=i[:-1]
    words=i.split(" ")
    total_word=len(words)
    outfile=open("Temp_list_of_query_with_"+str(total_word)+"_words.txt","a")
    outfile.write(i+"\n")
    outfile.close()
    
final_output=open("synthetic4_random_0.1m_001_stemmed_updated.txt","w")
for i in range(1,max_words+1):
    temp_inputfile=open("Temp_list_of_query_with_"+str(i)+"_words.txt","r")
    temp_file_lines=temp_inputfile.readlines()
    no_records_req=(len(temp_file_lines)*100000)/total_records
    templist=random.sample(temp_file_lines,no_records_req)
    temp_inputfile.close()

    for i in templist:
        final_output.write(i)

final_output.close()
    
