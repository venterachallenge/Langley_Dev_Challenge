'''
Ben Langley
October 24th, 2018

Ventera Dev Challenge

Description: This file reads in the JSON (in new format), analyzes certain metrics
and displays the results in the command line for the user
'''
from transform import transform

######################
## Global Variables ##
######################
inputJSONFile = "data.json"
outputJSONFile = "transformed.json"

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
		self.data = data

	'''
	Get a list of unique vendor names

	returns list of unique vendors
	'''
	def getVendorNames(self):
		names = [] # List to store names in

		# Loop over each transaction and get the vendor name
		for item in self.data:
			names.append(item["vendor"])

		# Remove duplicates by making a set then back to a list
		return list(set(names))


	'''
	Compute the total revenue of each vendor

	returns dictionary of each vendor and their total revenue
	'''
	def computeTotalRevenueByVendor(self):
		# Initialize the revenue data structure
		revenue = {}
		for vendor in self.getVendorNames():
			revenue[vendor] = 0

		# Compute total revenue of all vendors
		for transaction in self.data:
			vendor = transaction["vendor"]

			# Get the transaction total revenue
			for item in transaction["details"]:
				revenue[vendor] += item["revenue"]

		return revenue


	'''
	Get the vendor with the heightest revenue

	revenueDict - dictionary of total revenue by vendor
		Output of computeTotalRevenueByVendor()
	returns the name of the vendor witht he heighest revenue
	'''
	def getHeighestRevenueVendor(self, revenueDict):
		# Initialize the maximums
		maxKey = ""
		maxRevenue = 0

		# Find maximum value and return key by iterating over
		# each (vendor, revenue) pair in the dictionary
		for vendor, revenue in revenueDict.items():
			if (revenue > maxRevenue):
				maxRevenue = revenue
				maxKey = vendor

		# Return vendor of the maximum revenue
		return maxKey


	'''
	Compute the total number of sales for a specific item

	itemKey - the exact key to match for computing number of items sold
	returns the total number of items sold for the given item key
	'''
	def computeItemsSold(self, itemKey):
		# Initialize the items sold counter 
		total = 0

		# Iterate over each transaction
		for transaction in self.data:
			# Iterate over each item in transaction
			for item in transaction["details"]:
				if (item["item"] == itemKey):
					total += item["quantity"]

		return total


	'''
	Find the customer who bought the most of a specific item in given month

	itemKey - the exact key to match for the item to find customer for
	month - the integer month to verify transactions in
	returns the customerID who bought the most of the item given by itemKey
	'''
	def customerBoughtMostItem(self, itemKey, month):
		# Initialize a dictionary of customers to store ID and matching items bought
		customersDict = {}

		# Iterate over each transaction to populate customers dict
		for transaction in self.data:
			customerID = transaction["customerID"]
			# Verify month is correct
			trans_month = int(transaction["date"][0:2])
			if (trans_month == month):
				# Continue checking for item in transaction
				for item in transaction["details"]:
					# Verify correct item
					if (item["item"] == itemKey):
						# Update the customer dict
						if customerID in customersDict:
							customersDict[customerID] += item["quantity"]
						else:
							customersDict[customerID] = item["quantity"]

		# Find customer with max
		maxCustomer = ""
		maxItems = 0

		# Find maximum value and return key by iterating over
		# each (customer, items count) pair in the dictionary
		for customer, items in customersDict.items():
			if (items > maxItems):
				maxItems = items
				maxCustomer = customer

		# Return customer of the maximum items bought
		return maxCustomer


'''
Main function to run the data provided for the challenge
'''
def main():
	# Get the data in the transformed form
	data = transform(inputJSONFile, outputJSONFile)

	# Create the Vendor Data object
	vendor_data = VendorData(data)
	vendor_revenue = vendor_data.computeTotalRevenueByVendor()

	# Print the challenge specific data
	print("Total Revenue: ", sum(vendor_data.computeTotalRevenueByVendor().values()))
	print("Vendor with Heighest Revenue: ", vendor_data.getHeighestRevenueVendor(vendor_revenue))
	print("Quantity of Hats Sold: ", vendor_data.computeItemsSold("hat"))
	print("Customer who Bought Most Ice (October): ", vendor_data.customerBoughtMostItem("ice", 10))
	
# Run the method!
main()

