import pickle
import string

# Storing the distinct words in the file in a dictionary
for index in range(1,2):
    try:
        #filename="synthetic3_random_stemd_0.1m_"+str(index)+".txt"
        #filename="synthetic8_random_stemd_1m_"+str(index)+".txt"
        #filename="synthetic8_random_stemd_0.1m_"+str(index)+".txt"
        #filename="synthetic9_random_stemd_1m_"+str(index)+".txt"
        filename="synthetic9_random_stemd_0.1m_"+str(index)+".txt"
        file_to_dict=open(filename,"r")
        #lines = file_to_dict.readlines()
        worddict={}
        counter=1
        for i in file_to_dict:
            i=i.strip("\n") #for removing space and /n at the end of a line
            i=i.strip(" ")
            words = i.split(" ") #splitting lines into words
            for j in words[0:]:  #indexing the word
                if worddict.has_key(j):
                    pass
                else:
                    worddict[j]=counter
                    counter=counter+1

        file_to_dict.close()
    except IOError :
        print "The filename doesnt exist.Please check"

    #Storing the words in the dictionary in the file
    #listname="synthetic1_0.1m_list_for_"+str(index)+".txt"
    #listname="synthetic8_1m_list_for_"+str(index)+".txt"
    #listname="synthetic8_0.1m_list_for_"+str(index)+".txt"
    #listname="synthetic9_1m_list_for_"+str(index)+".txt"
    listname="synthetic9_0.1m_list_for_"+str(index)+".txt"
    dict_to_file=open(listname,"w") 
    pickle.dump(worddict,dict_to_file)  
    dict_to_file.close()

    #Creating a file in which the words present in source file are stored as their
    #counter values in another file
    try:
        readfile=open(filename,"r")
        #wordval="synthetic1_random_0.1m_valued_"+str(index)+".txt"
        #wordval="synthetic8_random_1m_valued_"+str(index)+".txt"
        #wordval="synthetic8_random_0.1m_valued_"+str(index)+".txt"
        #wordval="synthetic9_random_1m_valued_"+str(index)+".txt"
        wordval="synthetic9_random_0.1m_valued_"+str(index)+".txt"
        word_to_val=open(wordval,"w")
        #rlines=readfile.readlines()
        for i in readfile:
            i=i.strip("\n")
            i=i.strip(" ")
            words = i.split(" ")
            for j in words[0:]:
                val=str(worddict[j])
                word_to_val.write(val)
                word_to_val.write(" ")
            word_to_val.write("\n")
        readfile.close()
        word_to_val.close()
    except IOError :
        print "The filename doesnt exist.Please check"

