#!/usr/bin/env python3

""" Populates a dictionary of order names and taxa. 
Able to index multiple values to a key
Practical 1, Week 2 """

__author__ = 'Merry Crowson'
__version__ = '0.0.1'


# data

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:

taxa_dic = {}

for value, key in taxa:
        #Initialize empty list if key doesn't exist
        if key not in taxa_dic:
                taxa_dic[key] = []
        # Now we know the key always exists
        taxa_dic[key].append(value)
print(taxa_dic)


#how to do it as conditional statement?
#taxa_dic = dict({t[1]:set([t[0]]) for t in taxa}) # Only one value per key
#print(taxa_dic)


#dict([(a,b) for b, a in taxa])

