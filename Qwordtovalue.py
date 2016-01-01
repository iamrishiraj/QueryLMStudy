import pickle
import string

# Storing the distinct words in the file in a dictionary
try:
    file_to_dict=open("AnjanaQueries.txt","r")
    lines = file_to_dict.readlines()
    worddict={}
    counter=1
    for i in lines:
        words = i.split(" ") #splitting lines into words
        for j in words[0:]:  #indexing the word
            if worddict.has_key(j):
                pass
            elif (j[-1]=='\n' and worddict.has_key(j[0:-1])): #check for whether the word contains \n at the end
                pass
            else:
                if j[-1]=='\n':
                    worddict[j[0:-1]]=counter
                    counter=counter+1
                else:
                    worddict[j]=counter
                    counter=counter+1
    file_to_dict.close()
except IOError :
    print "The filename doesnt exist.Please check"

#Storing the words in the dictionary in the file
dict_to_file=open("unstemwordlist.txt","w") 
pickle.dump(worddict,dict_to_file)  
dict_to_file.close()

#Creating a file in which the words present in source file are stored as their
#counter values in another file
try:
    readfile=open("AnjanaQueries.txt","r")
    word_to_val=open("AnjanaQueriesvalued.txt","w")
    rlines=readfile.readlines()
    for i in rlines:
        words = i.split(" ")
        for j in words[0:]:
            if j[-1]=='\n':
                val=str(worddict[j[:-1]])
            else:
                val=str(worddict[j])
            word_to_val.write(val)
            word_to_val.write(" ")
        word_to_val.write("\n")
    readfile.close()
    word_to_val.close()
except IOError :
    print "The filename doesnt exist.Please check"
