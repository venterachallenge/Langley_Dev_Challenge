'''
Ben Langley
October 24th, 2018

Ventera Dev Challenge

Description: This file contains wrapper functions for JSON methods
to be used to easily access the read/write capabailites of the JSON
class in python
'''
import json

'''
Helper function to save the JSON data to the give file

data - the JSON data to save
outputfile - the output file to write to
'''
def saveJSON(data, outputfile):


'''
Helper function to get the JSON data from the given file

inputfile - the file to read JSON data from
returns JSON object of the data
'''
def getJSON(inputfile):