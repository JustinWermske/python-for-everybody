# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

handle = open('regex_sum_2149373.txt')
numlist = list()
# loop through each line in the file
for line in handle:
    line = line.rstrip() # Remove trailing whitespace
    stuff = re.findall('[0-9]+', line)  # Find all numbers in the line
    for number in stuff:
        numlist.append(int(number))  # Convert each found number to an integer and add to the list
print(sum(numlist))  # Print sum of all numbers found in the file
