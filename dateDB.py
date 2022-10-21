# Author: Soundarya Srinivasagan
# Date: October 20th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help create the date feature for this program, so, we can later give a customized date to pay all credit balences

import psycopg2
import re
from mainDB import *
from creditDB import *
from report import *

# This will help identify which DB the action should take place in for credit card information
creditCard = "creditcard"
loc = "loc"
other = "other"

# This will help identify which DB the action should take place in for statement date information
creditCardDate = "creditcarddate"
locDate = "locdate"
otherDate = "otherdate"

newline= "\n"

credit = "Credit Card"
lineOfCredit = "Line of Credit"
otherCredit = "Other Types of Credit Card"

creditCardDict_date = {}
creditLineOfCreditDict_date = {}
creditOtherDict_date = {}

def dateDetails(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict):
    print("*************************************************************************************************************")
    print("The following section will collect details on your when your statement generates for all your credit sources")
    print("*************************************************************************************************************")

    # Query each credit database and output a new database with the dates
    # Credit Card Database
    getCreditInfoFromDict(val_tableName, val_userName, creditCardDict, creditCard)
    getCreditInfoFromDict(val_tableName, val_userName, creditOtherDict, other)

    # Generate Credit info for userNamer
    #################################################################################################
    # Get credit information from database for user
    credit_card = getCreditInfo(val_tableName, val_userName, creditCardDict, creditCard)
    # Convert and modify headers list from tuple to list of strings
    card_card_TupToString = convertTupToStringMod(credit_card)
    # Get credit headers from database for user
    credit_card_headers = getCreditHeadersInDB(val_tableName, creditCard)
    # Convert and modify headers list from tuple to list of strings
    card_headers = convertTupToStringMod(credit_card_headers)

    print ("Credit Card Statement Generation Details")
    print ("-------------------------------------------")
    count = 0
    for (i, j) in zip(card_headers, card_card_TupToString):
        if (("id" not in i) and (val_userName not in j) and (count == 0)):
            print(i + " = " + j)
            generate = input("When does the statement generate for this product? [ Enter day of the month, for example: 15 ] -->  ")
            creditCardDict_date.update({i: generate})
            createTable(val_tableName, val_userName, creditCardDict_date, creditCardDate)
            print(i + " = " + j + " -----> " + generate)
            count = count + 1

        elif(("id" not in i) and (val_userName not in j)):
            print(i + " = " + j)
            generate = input("When does the statement generate for this product? [ Enter day of the month, for example: 15 ] -->  ")
            creditCardDict_date.update({i: generate})
            MapVal(val_tableName, val_userName, creditCardDict_date, creditCardDate)
            print(i + " = " + j + " -----> " + generate)
            count = count + 1

    # Line of Credit loans do not have a grace period

    # Generate Other types of Credit info for userNamer
    #################################################################################################
    other_credit = getCreditInfo(val_tableName, val_userName, creditOtherDict, other)
    # Convert and modify headers list from tuple to list of strings
    card_other_TupToString = convertTupToStringMod(other_credit)
    # Get credit headers from database for user
    other_credit_headers =getCreditHeadersInDB(val_tableName, other)
    # Convert and modify headers list from tuple to list of strings
    other_headers = convertTupToStringMod(other_credit_headers)

    print ("Other Credit Card Statement Generation Details")
    print ("-----------------------------------------------")
    countt = 0
    for (i, j) in zip(other_headers, card_other_TupToString):
        if (("id" not in i) and (val_userName not in j) and (count == 0)):
            print(i + " = " + j)
            generate = input("When does the statement generate for this product? [ Enter day of the month, for example: 15 ] -->  ")
            creditOtherDict_date.update({i: generate})
            createTable(val_tableName, val_userName, creditOtherDict_date, otherDate)
            print(i + " = " + j + " -----> " + generate)
            countt = countt + 1

        elif(("id" not in i) and (val_userName not in j)):
            print(i + " = " + j)
            generate = input("When does the statement generate for this product? [ Enter day of the month, for example: 15 --> ]  ")
            creditOtherDict_date.update({i: generate})
            MapVal(val_tableName, val_userName, creditOtherDict_date, otherDate)
            print(i + " = " + j + " -----> " + generate)
            countt = countt + 1


def getCreditInfoFromDict(val_tableName, val_userName, dict, type):
    local_cursor = connectToDB()
    sql_id = """SELECT * FROM """ + val_tableName + """_""" + type + """ WHERE id = """ + """ \' """ + val_userName + """ \' """ + """ ; """
    local_cursor.execute(sql_id)
    results = local_cursor.fetchall()

    return results

def createTable(val_tableName, val_userName, dict, type):
    creditTableDB(val_tableName, val_userName, dict, type)
    insertValToIdUser_Credit(val_tableName, val_userName, dict, type)

def MapVal(val_tableName, val_userName, dict, type):
    # Query to check whether the table already exits
    local_cursor = connectToDB()
    sql_id = """SELECT EXISTS ( SELECT FROM information_schema.tables """ + """ WHERE table_name = """ + """ \'""" + val_tableName + """_""" + type + """\'""" + """);"""
    local_cursor.execute(sql_id)
    result = local_cursor.fetchall()
    results = convertTupToStringMod(result)

    # Check to see if table already exists
    if ( "Tru" in results):
        # Add extra rows
        updateCreditDBOtherUser(val_tableName, val_userName, dict, type)
        # Insert values into rows
        insertDataDBOtherPayments(val_tableName, val_userName, dict, type)
    else:
        # If table already exits, the code goes here
        creditTableDB(val_tableName, val_userName, dict, type)
        # Add extra rows
        insertValToIdUser_Credit(val_tableName, val_userName, dict, type)
        # Insert values into rows
        insertDataDBOtherPayments(val_tableName, val_userName, dict, type)

## RESOLVE IMPORT ERROR AND TAKE OFF THE FOLLOWING FUNCTIONS FROM BELOW
#########################################################################
def creditTableDB(val_tableName, val_userName, dict, type):
    local_cursor = connectToDB()

    # Create table statement
    sqlCreateTable1 = """ CREATE TABLE """ + val_tableName + """_""" + type
    sqlCreateTable2 = """ ( id """ + """ text, """

    key = list(dict.keys())
    lastElement = key[-1]

    part = """  """
    for keys, values in dict.items():
        part12 = keys
        part14 = """ text """
        part_space = """  """
        if (keys == lastElement):
            part13 = """  """
            part = part + part12 + part_space + part14 + part13
        else:
            part13 = """ , """
            part = part + part12 + part_space + part14 + part13

    sqlCreateTable3 = part
    sqlCreateTable4 = """ ); """
    sqlCreateTable = sqlCreateTable1 + sqlCreateTable2 + sqlCreateTable3 + sqlCreateTable4

    # Create a table in PostgreSQL database
    local_cursor.execute(sqlCreateTable)


#########################################################################
def insertValToIdUser_Credit(tableName, val_userName, dict, type):
    local_cursor = connectToDB()
    key = list(dict.keys())
    lastElement = key[-1]

    # Use Update statement so that the same row could be updated
    postgres_insert_query_1T = """ INSERT INTO """ + tableName + """_""" + type + """ ( id, """
    postgres_insert_query_2T = """  """
    postgres_insert_query_3T = """  VALUES ( """ + """ \' """  + val_userName + """ \', """ + """ """

    # Map keys into Insert Into SQL statement
    for keys in dict:
        part1 = """ = """
        if (keys == lastElement):
            part4 = """ ) """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part4
        else:
            part4 = """ , """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part4

    # Map values into Insert Into SQL statement
    part_val = """ \' """
    postgres_insert_query_2TT = """  """
    for keys, values in dict.items():
        if (keys == lastElement):
            part41 = """ \' ); """
            postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values + part41
        else:
            part41 = """ \', """
            postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values  + part41

    postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_2T + postgres_insert_query_3T + postgres_insert_query_2TT
    local_cursor.execute(postgres_insert_query)

#########################################################################
def updateCreditDBOtherUser(tableName, userName, dict, type):
    local_cursor = connectToDB()

    # Alter Table to add more columns
    key = list(dict.keys())
    lastElement = key[-1]

    # Use Update statement so that the same row could be updated
    postgres_insert_query_1T = """ ALTER TABLE """ + tableName + """_""" + type
    postgres_insert_query_2T = """  """
    postgres_insert_query_3T = """ ADD """
    postgres_insert_query_4T = """ ; """

    for keys in dict:
        # Check to see if key exists already in database headers
        results = getCreditHeadersInDB(tableName, type)
        card_headers_results = convertTupToStringMod(results)
        print(card_headers_results)
        # By looking at keys not in dict, we can add a new column to the database if it doesn't exist
        if (keys not in card_headers_results):
            type = """ text """
            # space = """  """
            if (keys == lastElement):
                part4 = """  """
                postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4
            else:
                part4 = """ , """
                postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4 + postgres_insert_query_3T

    postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_3T + postgres_insert_query_2T + postgres_insert_query_4T
    print(postgres_insert_query)
    local_cursor.execute(postgres_insert_query)


#########################################################################
def insertValToIdUser_Credit(tableName, val_userName, dict, type):
    local_cursor = connectToDB()
    key = list(dict.keys())
    lastElement = key[-1]

    # Use Update statement so that the same row could be updated
    postgres_insert_query_1T = """ INSERT INTO """ + tableName + """_""" + type + """ ( id, """
    postgres_insert_query_2T = """  """
    postgres_insert_query_3T = """  VALUES ( """ + """ \' """  + val_userName + """ \', """ + """ """

    # Map keys into Insert Into SQL statement
    for keys in dict:
        part1 = """ = """
        if (keys == lastElement):
            part4 = """ ) """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part4
        else:
            part4 = """ , """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part4

    # Map values into Insert Into SQL statement
    part_val = """ \' """
    postgres_insert_query_2TT = """  """
    for keys, values in dict.items():
        if (keys == lastElement):
            part41 = """ \' ); """
            postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values + part41
        else:
            part41 = """ \', """
            postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values  + part41

    postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_2T + postgres_insert_query_3T + postgres_insert_query_2TT
    local_cursor.execute(postgres_insert_query)

#########################################################################
def insertDataDBOtherPayments(tableName, user, dictOfValues, type):
    local_cursor = connectToDB()

    key = list(dictOfValues.keys())
    lastElement = key[-1]

    # Use Update statement so that the same row could be updated
    postgres_insert_query_1T = """ UPDATE """ + tableName + """_""" + type + """ SET """
    postgres_insert_query_2T = """  """
    postgres_insert_query_3T = """  WHERE id = """ + """ ' """ + user + """ ' """
    postgres_insert_query_4T = """ ; """
    for keys, values in dictOfValues.items():
        part1 = """ = """
        if (keys == lastElement):
            part4 = """  """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part1 + values + part4
        else:
            part4 = """ , """
            postgres_insert_query_2T = postgres_insert_query_2T + keys + part1 + values + part4

    postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_2T + postgres_insert_query_3T + postgres_insert_query_4T
    local_cursor.execute(postgres_insert_query)
