#!/usr/bin/env python3

"""This script aligns two DNA sequences 
such that they are as similar as possible"""

#__format#__ is used for this only, not for variable names
__appname__ = 'Align_DNA' #Application is nother name for program
__author__ = 'Samraat I think'
__version__ = '0.0.1'

# imports

import csv

# These are the two sequences to match
 
seq2 = str()
seq1 = str()
 
with open("../Data/DNA.txt") as csvDataFile: #There must be a better way!
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        seq2 = row[0]
        seq1 = row[1]
 

# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest

l1 = len(seq1) # length of seq1
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths


# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # build some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print("")

    return score

calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1)
calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1

for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2
        my_best_score = z

print(my_best_align)
print(s1)
print("Best score:", my_best_score)

with open("alig_seqs_best_resut.txt", "w") as text_file:
    text_file.write("The best alignment is:\n%s\n%s\nBest score: %s" % (my_best_align, s1, my_best_score))

print("Best result has been saved as 'alig_seqs_best_resut.txt'")

