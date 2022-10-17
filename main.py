
# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

'''
# Creating the Database
import psycopg2
# pip3 install psycopg2-binary

# Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='soundarya', password='password', host='10.0.0.65', port= '5432'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
#sql = CREATE database increaseCreditScore;

# Creating a database
cursor.execute(sql)
print("Database created successfully...")

# Closing the connection
conn.close()
'''
#!/usr/bin/python
import psycopg2
import sys

def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"

	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print("Connected!\n")

if __name__ == "__main__":
	main()