# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2
from mainDB import *
from creditDB import *

if __name__ == "__main__":

	print("**********************************************************************************")
	print("Welcome to increaseCreditScore")
	print("Tool Description")
	print("**********************************************************************************")

	creditCardDict = {}
	creditLineOfCreditDict = {}
	creditOtherDict = {}

	# This will help identify which DB the action should take place in
	creditCard = "creditCard"
	loc = "loc"
	other = "other"

	option = input("""Please choose from the following options: 
	(1) Is this your first time running this program --> Type 1
	(2) Add user to database --> Type 2 
	(3) Configure bill payments --> Type 3 
	(4) Configure credit limits --> Type 4  
	(5) Get updated report --> Type 5 
	Choice = """)

	# First time running this program
	if ("1" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect(val_tableName, val_userName, True)

		# This will create and add details regarding your credit limit
		creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)
		mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)

	# Add user to database
	elif ("2" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect(val_tableName, val_userName, False)

	# Configure bill payments
	elif ("3" in option):
		print("**********************************************************************************")
		print("Please choose from the following:")
		val_option = input("""
		(1) Would you like to add additional credit cards --> Type 1
		(2) Would you like to update your current credit information --> Type 2 
		Choice = """)

	# Configure credit limits
	elif ("4" in option):
		print("**********************************************************************************")
		print("Please choose from the following:")
		val_option = input("""
		(1) Would you like to add your credit information --> Type 1
		(2) Would you like to update your credit information --> Type 2 
		Choice = """)

	# Get updated report
	elif ("5" in option):
		print("Soon to come")

# Other members part of the family can add data to the same DB
## Current problem = the DBs here are empty and you need to Alter and update the table
### Might become easier when you simplify code
# updateCreditDBOtherUser(val_tableName, val_userName, creditCardDict, creditCard)
# updateCreditDBOtherUser(val_tableName, val_userName, creditLineOfCreditDict, loc)
# updateCreditDBOtherUser(val_tableName, val_userName, creditOtherDict, other)
