'''
Ben Langley
October 24th, 2018

Ventera Dev Challenge

Description: This file reads in the JSON (in new format), analyzes certain metrics
and displays the results in the command line for the user
'''
from transform import transform


'''
Class to wrap the vendor data 

These methods were added to the class because most of them
required the data attribute so I abstracted it away into this
new class to store the Vendor Data
'''
class VendorData(object):

	'''
	Initalize the vendor data instance with the given data
	'''
	def __init__(self, data):

	'''
	Get a list of unique vendor names from the JSON data

	data - the JSON data
	returns list of unique vendors
	'''
	def getVendorNames(self):


	'''
	Compute the total revenue of each vendor from the data given

	data - the JSON data
	returns dictionary of each vendor and their total revenue
	'''
	def computeRevenue(self):


	'''
	Get the vendor with the heightest revenue

	revenueDict - dictionary of each vendor and their total revenue
		Output from computeRevenue() is correct format
	returns the name of the vendor witht he heighest revenue
	'''
	def getHeighestRevenueVendor(self, revenueDict):


	'''
	Compute the total number of sales for a specific item

	itemKey - the exact key to match for computing number of items sold
	returns the total number of items sold for the given item key
	'''
	def computeItemsSold(self, itemKey):


	'''
	Find the customer who bought the most of a specific item

	itemKey - the exact key to match for the item to find customer for
	returns the customerID who bought the most of the item given by itemKey
	'''
	def customerBoughtMostItem(self, itemKey):


'''
Main function to run the data provided for the challenge
'''
def main():

