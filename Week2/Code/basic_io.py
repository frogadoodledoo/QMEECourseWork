##########################
# FILE INPUT
##########################
# Open a file for reading
f = open('../Sandbox/test.txt', 'r') #The .. moves you one directory up. You should be in the foulder Code.
#use "implicit" for loop:
# if the object is a file, python will cycle over lines

for line in f:
    print(line)

# close the file
f.close() #Closes it in your RAM

# Same example, skip blank lines
f = open('../Sandbox/test.txt', 'r')
for line in f:
    if len(line.strip()) > 0:
        print(line)
f.close()



##########################
# File output
##########################
#Save the elements of a list to a file
list_to_save = range(100)

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') #Add a new line at the end

f.close()



##########################
# Storing object
##########################

# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle # this saves the python object exactly as it is. It can't be opened by other programmes. A bit like .Rdata or .m

f = open('../Sandbox/testp.p', 'wb') ## note the b: accept binar
pickle.dump(my_dictionary, f)
f.close()



