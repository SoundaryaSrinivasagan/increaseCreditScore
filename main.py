# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2
import sys
import pandas

# Define our connection string
conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

# Get a connection, if a connection cannot be made, an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
conn.autocommit = True
cursor = conn.cursor()

name_Table = "news_stories12"

# Create table statement
#sqlCreateTable = "create table " + name_Table + " (id bigint, title varchar(128), summary varchar(256), story text);"

# Create a table in PostgreSQL database
#cursor.execute(sqlCreateTable)
#conn.commit()

sql= """ SELECT * FROM news_stories1; """

cursor.execute(sql)
column_names = [desc[0] for desc in cursor.description]

for i in column_names:
    print(i)

conn.commit()
conn.close()
