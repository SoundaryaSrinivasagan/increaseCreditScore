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
at =   """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \n"""
newline= "\n"

# This will help identify which DB the action should take place in
creditCard = "creditcard"
loc = "loc"
other = "other"

credit = "Credit Card"
lineOfCredit = "Line of Credit"
otherCredit = "Other Types of Credit Card"

# This will help identify which DB the action should take place in for statement date information
creditCardDate = "creditcarddate"
locDate = "locdate"
otherDate = "otherdate"

def reportGenerate(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict):
    # Generate the header in the text file
    generateHeader(val_userName, val_tableName)

    # Section 1: How much should I spend?
    ##################################################
    with open('report.txt', 'a') as f:
        f.write("SECTION 1:\n")
        f.write(at)
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

    # Section 2: When should I pay my Credit Cards?
    ##################################################
    with open('report.txt', 'a') as f:
        f.write("SECTION 2:\n")
        f.write(at)
        f.write("When should I pay my Credit Cards?")
        f.write(newline)
        f.write(newline)

        # Query from both credit date databases and store them as a list
        # Generate Credit info for userNamer
        #################################################################################################
        # Get credit information from database for user
        credit_card_date = getCreditInfo(val_tableName, val_userName, creditCardDict, creditCardDate)
        # Convert and modify headers list from tuple to list of strings
        card_card_TupToString_date = convertTupToStringMod(credit_card_date)
        # Get credit headers from database for user
        credit_card_headers_date = getCreditHeadersInDB(val_tableName, creditCardDate)
        # Convert and modify headers list from tuple to list of strings
        card_headers_date = convertTupToStringMod(credit_card_headers_date)

        # Store the db in a dict
        d_creditdate = {}
        for (i,j) in zip(card_headers_date,card_card_TupToString_date):
            singleDicts = dict(zip([i], [j]))
            d_creditdate.update(singleDicts)

        # Generate Other types of Credit info for userNamer
        #################################################################################################
        other_credit_date = getCreditInfo(val_tableName, val_userName, creditOtherDict, otherDate)
        # Convert and modify headers list from tuple to list of strings
        card_other_TupToString_date = convertTupToStringMod(other_credit_date)
        # Get credit headers from database for user
        other_credit_headers_date = getCreditHeadersInDB(val_tableName, otherDate)
        # Convert and modify headers list from tuple to list of strings
        other_headers_date = convertTupToStringMod(other_credit_headers_date)

       # Store results in d_creditdate
        for (i,j) in zip(other_headers_date, card_other_TupToString_date):
            singleDicts = dict(zip([i], [j]))
            d_creditdate.update(singleDicts)

        # Delete id from dictionary
        del d_creditdate['id']
        print(d_creditdate)

        for k,v in d_creditdate.items():
            d_creditdate.update({k : int(v)})

        # Max and min from dict
        key_max = max(d_creditdate.keys(), key=(lambda k: d_creditdate[k]))
        key_min = min(d_creditdate.keys(), key=(lambda k: d_creditdate[k]))

        # Considering that there is on average a 21-day grace period
        # If min + 15 (days considering bank holidays) < max, we need to pay it off before max date
        f.write("Recommended day to pay full statement balance or atleast minimum payment \n")
        f.write("------------------------------------------------------------------------- \n")
        minn_dict = {}
        max_dict = {}
        datee = 0
        minimumValue = d_creditdate[key_min]
        maximumValue = d_creditdate[key_max]
        minn = minimumValue + 15
        if (minn <= maximumValue):
            for k,v in d_creditdate.items():
                if (v < minn):
                    minn_dict.update({k:v})
                else:
                    max_dict.update({k:v})

            f.write("The following credit cards: ")
            for item in minn_dict:
                f.write(item + ", ")
            f.write("should be paid off by this day of each month: " + str(minn))
            f.write(newline)
            # For Max dates
            f.write("The following credit cards: ")
            for item in max_dict:
                f.write(item + ", ")
            f.write("should be paid off by this day of each month: " + str(maximumValue))
            f.write(newline)
        else:
            f.write("The following credit cards: ")
            for item in d_creditdate:
                f.write(item + ", ")
            f.write("should be paid off by this day of each month: " + str(minn))


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