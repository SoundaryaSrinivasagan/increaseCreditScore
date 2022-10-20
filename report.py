# Author: Soundarya Srinivasagan
# Date: October 19th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help create the final report

import psycopg2
from mainDB import *
from creditDB import *

line = """*************************************************************************************************** \n"""
dots = """................................................................................................... \n"""
newline= "\n"

# This will help identify which DB the action should take place in
creditCard = "creditcard"
loc = "loc"
other = "other"


def reportGenerate(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict):
    # Generate the header in the text file
    generateHeader()

    with open("report.txt", "a") as f:
        f.write(newline)
        f.write("This Report has been generated for: " + val_userName + newline)
        f.write("[" + val_userName + " belongs to group: " + val_tableName + "]" + newline)
        f.write(dots)

        # Print out all the data that userName has in a list format
        # result = printMainDB(val_tableName, val_userName)
        # f.writelines([f"{line}\n" for line in result])

        # Generate Credit info for userNamer
        credit_card = getCreditInfo(val_tableName, val_userName, creditCardDict, creditCard)
        credit_card_headers = getCreditHeadersInDB(val_tableName, creditCard)
        f.write("Credit Card Headers: \n")
        f.writelines([f"{line}\n" for line in credit_card_headers])
        x = ', '.join(map(str, credit_card_headers))
        print(x)
        print(type(x))

        # tups = [(1, 2), (3, 4)]
        # print (', '.join(map(str, credit_card_headers)))
       # '(1, 2), (3, 4)'

        line_of_credit = getCreditInfo(val_tableName, val_userName, creditLineOfCreditDict, loc)
        line_of_credit_headers = getCreditHeadersInDB(val_tableName, loc)
        f.write("Line of Credit Headers: \n")
        f.writelines([f"{line}\n" for line in line_of_credit_headers])

        other_credit = getCreditInfo(val_tableName, val_userName, creditOtherDict, other)
        other_credit_headers =getCreditHeadersInDB(val_tableName, other)
        f.write("Other Types of Credit Card Headers: \n")
        f.writelines([f"{line}\n" for line in other_credit_headers])


def generateHeader():
    with open('report.txt', 'w') as f:
        f.write(newline)
        f.write(line)
        f.write(" Welcome to increaseCreditScore \n")
        f.write(" This program will help the user strategize their credit to effectively increase credit score\n")
        f.write(line)
        f.write(newline)

def printMainDB(val_tableName, val_userName):
    #listResults = printValuesInTable(val_tableName, val_userName)
    local_cursor = connectToDB()
    sql_id = """SELECT * FROM """ + val_tableName + """ WHERE id = """ + """ \' """ + val_userName + """ \' """ + """ ; """
    local_cursor.execute(sql_id)
    results = local_cursor.fetchall()

    return results

def getCreditInfo(val_tableName, val_userName, dict, type):
    local_cursor = connectToDB()
    sql_id = """SELECT * FROM """ + val_tableName + """_""" + type + """ WHERE id = """ + """ \' """ + val_userName + """ \' """ + """ ; """
    local_cursor.execute(sql_id)
    results = local_cursor.fetchall()

    with open('report.txt', 'a') as f:
        f.writelines([f"{line}\n" for line in results])

def getCreditHeadersInDB(val_tableName, type):
    local_cursor = connectToDB()
    sql = """SELECT COLUMN_NAME FROM """ + """ INFORMATION_SCHEMA.COLUMNS """ + """ WHERE TABLE_NAME = """ + """ \'""" + val_tableName + """_""" + type + """\' """ + """ ORDER BY ORDINAL_POSITION """ + """ ; """
    local_cursor.execute(sql)
    results = local_cursor.fetchall()

   # with open('report.txt', 'a') as f:
   #    f.writelines([f"{line}\n" for line in results])

    return results