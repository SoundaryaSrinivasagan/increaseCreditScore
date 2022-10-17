
# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2
import sys

def main():
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	sql = ''' CREATE TABLE increasecreditscore.test(); '''
	sql1 = ''' SELECT *  from increasecreditscore.test; '''
	cursor.execute(sql)
	print(cursor.execute(sql1))

if __name__ == "__main__":
	main()