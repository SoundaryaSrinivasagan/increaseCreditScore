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

	# Future version: check for invalid characters as input
	val = input("Is this your first time running this program: [yes | no] ")
	if ("yes" in val):
		val_tableName = input("Please enter your Group Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect_firstTime(val_tableName, val_userName, True)

	elif("no" in val):
		val_tableName = input("Please enter your Group Name: ")
		val_decide = input("Do you want to update amount for bill payments [1] or Add user to your Family Table [2]: [ 1 | 2 ]  ")
		if ("1" in val_decide):
			val_userName = input("What is your name: ")
			# val_update = input("What payment would you like to update: ")

			creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)
			mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)

		elif ("2" in val_decide):
			val_userName = input("What is your name: ")
			# This will not create a new group and add val_username to the same group
			query_billsCollect_firstTime(val_tableName, val_userName, False)

			# Other members part of the family can add data to the same DB
			## Current problem = the DBs here are empty and you need to Alter and update the table
			### Might become easier when you simplify code
			# updateCreditDBOtherUser(val_tableName, val_userName, creditCardDict, creditCard)
			# updateCreditDBOtherUser(val_tableName, val_userName, creditLineOfCreditDict, loc)
			# updateCreditDBOtherUser(val_tableName, val_userName, creditOtherDict, other)
