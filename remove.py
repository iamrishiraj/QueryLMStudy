filename=open("remove_unwanted_files.sh","w")
for i in range(1,101):
    string="rm artificial_random_1m_"+str(i)+"_unl_edglist.txt"
    filename.write(string)
    filename.write("\n")
filename.close()

