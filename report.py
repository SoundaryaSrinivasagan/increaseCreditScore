# Author: Soundarya Srinivasagan
# Date: October 19th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help create the final report

import re
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

credit = "Credit Card"
lineOfCredit = "Line of Credit"
otherCredit = "Other Types of Credit Card"

def reportGenerate(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict):
    # Generate the header in the text file
    generateHeader(val_userName, val_tableName)

    with open('report.txt', 'a') as f:
        f.write("SECTION 1:\n")
        f.write(dots)
        f.write("How much should I spend?")
        f.write(newline)
        f.write(newline)

    # Print out all the data that userName has in a list format
    # result = printMainDB(val_tableName, val_userName)
    # f.writelines([f"{line}\n" for line in result])

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
    # Print the value beside the header in the report
    printValBesideHeader(val_userName, card_headers, card_card_TupToString,credit)

    # Generate Line of Credit info for userNamer
    #################################################################################################
    line_of_credit = getCreditInfo(val_tableName, val_userName, creditLineOfCreditDict, loc)
    # Convert and modify headers list from tuple to list of strings
    card_loc_TupToString = convertTupToStringMod(line_of_credit)
    # Get credit headers from database for user
    line_of_credit_headers = getCreditHeadersInDB(val_tableName, loc)
    # Convert and modify headers list from tuple to list of strings
    loc_headers = convertTupToStringMod(line_of_credit_headers)
    # Print the value beside the header in the report
    printValBesideHeader(val_userName, loc_headers, card_loc_TupToString,lineOfCredit)

    # Generate Other types of Credit info for userNamer
    #################################################################################################
    other_credit = getCreditInfo(val_tableName, val_userName, creditOtherDict, other)
    # Convert and modify headers list from tuple to list of strings
    card_other_TupToString = convertTupToStringMod(other_credit)
    # Get credit headers from database for user
    other_credit_headers =getCreditHeadersInDB(val_tableName, other)
    # Convert and modify headers list from tuple to list of strings
    other_headers = convertTupToStringMod(other_credit_headers)
    # Print the value beside the header in the report
    printValBesideHeader(val_userName, other_headers, card_other_TupToString, otherCredit)


def generateHeader(val_userName, val_tableName):
    with open('report.txt', 'w') as f:
        f.write(newline)
        f.write(line)
        f.write(" Welcome to increaseCreditScore \n")
        f.write(" This program will help the user strategize their credit to effectively increase credit score\n")
        f.write(line)

        f.write(newline)
        f.write("This report has been generated for: " + val_userName + newline)
        f.write("[" + val_userName + " belongs to group: " + val_tableName + "]" + newline)
        f.write(line + newline)

def printMainDB(val_tableName, val_userName):
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

    return results

def getCreditHeadersInDB(val_tableName, type):
    local_cursor = connectToDB()
    sql = """SELECT COLUMN_NAME FROM """ + """ INFORMATION_SCHEMA.COLUMNS """ + """ WHERE TABLE_NAME = """ + """ \'""" + val_tableName + """_""" + type + """\' """ + """ ORDER BY ORDINAL_POSITION """ + """ ; """
    local_cursor.execute(sql)
    results = local_cursor.fetchall()

    return results

def convertTupToStringMod(dict):
    convertTupToString = '.. '.join(map(str, dict))
    x = list(convertTupToString.split(","))
    part0 = []

    for item in x:
        part = str(item)[1:-1]
        part2 = re.sub('\W+', '', part)
        part0.append(part2)

    return part0

def printValBesideHeader(val_userName, credit_header_info, credit_dbinfo, type):
    with open("report.txt", "a") as f:
        f.write("Current " + type + " Information for " + val_userName + newline)
        f.write("------------------------------------------------------------- \n")
        for (i, j) in zip(credit_header_info, credit_dbinfo):
            if (("id" not in i) and (val_userName not in j)):
                f.write(i + " = $" + j + "      Spending Limit: $" + str(int(float(j)*0.30)) + newline)
        f.write(newline)