#!/usr/bin/env python3

""" Creates seperate lists of latin names, common names and mean body masses 
for each species in birds """

__author__ = 'Merry Crowson'
__version__ = '0.0.1'

## imports ##
import sys # module to interface our program with the operating system


# data
birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) list comprehensions

# Create list of latin names of each species in birds
latin_lc = list([species[0] for species in birds]) #Takes the first element [0] from each of the tuples (species) within the tuple "birds"
print(latin_lc) #returns a set

# Create list of common names of each species in birds
common_lc = list([species[1] for species in birds])
print(common_lc)

# Create list of mean body masses of each species in birds
bodymass_lc = list([species[2] for species in birds])
print(bodymass_lc)

#(2) For loops

# For loop of latin names of each species in birds
latin_loops = list() # initialise set
for species in birds:
    latin_loops.append(species[0]) #Takes the first element and appends it to the list "latin loops"
print(latin_loops)

# For loop of common names of each species in birds
common_loops = list()
for species in birds:
    common_loops.append(species[1])
print(common_loops)

# For loop of the mean body mass for each species in birds
bodymass_loops = list()
for species in birds:
    bodymass_loops.append(species[2])
print(bodymass_loops)


#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS.