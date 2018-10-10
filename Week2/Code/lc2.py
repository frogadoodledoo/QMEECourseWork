#!/usr/bin/env python3

""" Creates seperate lists of months and/or rainfall values based on certain criteria. Practical 1, Week 2 """

__author__ = 'Merry Crowson'
__version__ = '0.0.1'


#Data

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )


# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

rain_100_lc = tuple([month for month in rainfall if month[1] > 100]) 
print(rain_100_lc)
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

rain_100_lc = list([month[0] for month in rainfall if month[1] < 50]) 
print(rain_100_lc)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

rain_100_loops = tuple()
for month in rainfall:
    if month[1] > 100:
        rain_100_loops = rain_100_loops + month
print(rain_100_loops)


rain_50_loops = list()
for month in rainfall:
    if month[1] < 50:
        rain_50_loops.append(month[0])
print(rain_50_loops)


# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

