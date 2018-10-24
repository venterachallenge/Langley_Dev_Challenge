'''
Ben Langley
October 24th, 2018

Ventera Dev Challenge

Description: This file contains wrapper functions for JSON methods
to be used to easily access the read/write capabailites of the JSON
class in python
'''
import json
import pprint

'''
Helper function to save the data dictionary to the give file as JSON

data - the JSON data to save
outputfile - the output file to write to
'''
def saveAsJSON(data, outputfile):
	with open(outputfile, 'w') as outfile:
		json.dump(data, outfile)


'''
Helper function to get the JSON data from the given file

inputfile - the file to read JSON data from
returns JSON object of the data
'''
def getJSON(inputfile):
	with open(inputfile) as json_file:
	    json_data = json.load(json_file)
	    return json_data


'''
Main function for testing
'''
def main():
	data = getJSON("data.json")

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(data)

	saveAsJSON(data, "test.json")

# For DEBUG
#main()