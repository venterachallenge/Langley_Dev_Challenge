'''
Ben Langley
October 24th, 2018

Ventera Dev Challenge

Description: This file reads in the JSON in data.json, transforms it
per the details in the README and saves the new json to data-transformed.json
For more details on how to use this file please consult the read me

Note: If in the future there are multiple types of transforms, the given functions
should be abstrated to a class. This file can then contain multiple classes for
different transformations which can be loaded by external files on as needed basis
'''
import json
import JSONHelper


'''
Takes in customer JSON object in the old format and returns
just the customerID to be used in the new format

customer - the JSON customer details
returns the customerID as an integer
'''
def _transformCustomer(customer):


'''
Takes in order JSON object in the old format and returns a new
JSON object called details which is a list of order details

order - the JSON order details
returns the newly formated details as JSON
'''
def _transformOrder(order):


'''
Public function to transform the input json into the new format an save
to the outputfile

inputJSONfile - the input JSON file of the old format
	default: "data.json"
outputJSONfile - the output JSON file to save new format
	default: "transformed.json"
'''
def transform(inputJSONfile="data.json", outputJSONfile="transformed.json"):

'''
Main function - just for testing
'''
def main():