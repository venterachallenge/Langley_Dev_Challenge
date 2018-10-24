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
returns the customerID
'''
def _transformCustomer(customer):
	return customer["id"]


'''
Takes in order JSON object in the old format and returns a new
JSON object called details which is a list of order details

order - the JSON order details
returns the newly formated details as JSON 
'''
def _transformOrder(order):	
    transformed_items = [] # List of transformed items in the order 

    # Iterate over each item in the order
    for item, item_data in order.items():
    	# Transform the item
    	transformed_item_data = {}
    	transformed_item_data["item"] = item
    	transformed_item_data["quantity"] = item_data["quantity"]
    	transformed_item_data["price"] = item_data["price"]
    	transformed_item_data["revenue"] = item_data["quantity"] * item_data["price"]

    	# Append the transformed item to the list
    	transformed_items.append(transformed_item_data)

    return transformed_items


'''
Public function to transform the input json into the new format an save
to the outputfile

inputJSONfile - the input JSON file of the old format
	default: "data.json"
outputJSONfile - the output JSON file to save new format
	default: "transformed.json"
returns the transformed data dictionary
'''
def transform(inputJSONfile="data.json", outputJSONfile="transformed.json"):
	# Get the data
	data = JSONHelper.getJSON(inputJSONfile)

	# Transform the data
	transformed_data = [] # list of the transformed data items

	# Loop over each item in the data and transform
	for item in data:
		transformed_item = {} # the current item to be transformed
		transformed_item["id"] = item["id"]
		transformed_item["vendor"] = item["vendor"]
		transformed_item["date"] = item["date"]
		transformed_item["customerID"] = _transformCustomer(item["customer"])
		transformed_item["details"] = _transformOrder(item["order"])


		# Append the transformed item to the data list
		transformed_data.append(transformed_item)

	# Save the data
	JSONHelper.saveAsJSON(transformed_data, outputJSONfile)

	return transformed_data


# For DEBUG
#transform()