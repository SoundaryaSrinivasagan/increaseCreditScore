# Increase Credit Score
## <ins> Introduction

The `Increase Credit Score` tool was designed by me as a Proof-Of-Concept (POC) project to help users manage their credit spending 
and re-payment structure to effectively increase their credit score in the long run. The tool consists of two major components:
**Spending Limit** and **General Re-Payment Date**. The Spending Limit feature would take all the credit products that the user currently has and 
calculate a 30% limit that the user is recommended to use to effectively improve their credit in the long run. For example, if you have
a $1000 credit limit with the National Bank of Canada, you are recommended by *Transunion/Equifax/Government of Canada* to spend $300 of it a month.
Moreover, the General Re-Payment Date feature would take information on when the statement generates for each credit product and compute
a general day based on a 15-day grace period that the user can pay off their full balance or atleast make minimum payments. This would allow the user
to remember 1-2 days every month instead of multiple days based off their credit products.
    
**Sample Report**: ![architecture](https://user-images.githubusercontent.com/106931132/197216617-206f237a-7a0e-4424-9c87-e9b0b9432059.png)


__Targeted User:__ The product will be really useful for people with low to no credit or people that just want to increase their score in general.
The two major features of this product would one allow the user to condition themselves a new spending limit based on the 
recommended 30% limit in each credit product and two have a general day in each month that they user should remember to pay 
off statement balances for all their credit products.

__Technologies:__
> <span style = "color:green"> Git | Python | Unit Testing | PostgreSQL </span>

## <ins> Design
### Project Architecture

![my image](./assets/architecture.png)

#### < mainDB.py >
This file is responsible for creating/updating the group table in the main database. 

The main group database is: 

**groupName**: Contains information on all the bill payments that occur in a credit card for every user in the group

| Functions       | Description                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `connectToDB()` | This function returns a cursor which can be used to initiate a connection to the database and perform SQL operations                            |
| `connectDBCreateTable(name_Table, dictOfValues)`  | This function implements the CREATE TABLE SQL command                                                                                           |
| `insertDataDB(tableName, name, carInsurance, gym, internet, phone, loans)`  | This function implements the INSERT INTO SQL command                                                                                            |
| `insertDataDBOtherPayments(tableName, user, dictOfValues)`  | This function implements the UPDATE SQL command                                                                                                 |
| `printValuesInTable(val_tableName, val_userName)`  | This function returns all of the column headers in the database table as a list of tuple                                                        |
| `alterTableToAddMoreColumns(tableName, user, otherItemsList)`  | This function implements the ALTER TABLE SQL command                                                                                            |
| `query_billsCollect(val_tableName, val_userName, flag)`  | This function collects information on bill payments from the user and uses the other functions in this document to create/update the main table |


#### < creditDB.py >
This file is responsible for creating/updating the credit tables for the credit databases. 

The three credit databases are: 

**groupName_creditcard**: Contains information on the credit cards that every user of the group has

**groupName_loc**: Contains information on line of credit products that the every user of the group has

**groupName_other**: Contains information on other credit cards/products that every user of the group has

| Functions | Description                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)`    | This function collect credit product information from the user and stores the results into three dictionaries (credit card, line of credit, other credit products) |
| `creditTableDB(val_tableName, val_userName, dict, type)`    | This function implements the CREATE TABLE SQL command                                                                                                             |
| `insertValToIdUser_Credit(tableName, val_userName, dict, type)`    | This function implements the INSERT INTO SQL command                                                                                                              |
| `updateCreditDBOtherUser(tableName, userName, dict, type)`    | This function implements the ALTER TABLE SQL command                                                                                                              |
| `mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)`    | This function will call the `creditTableDB()` and `insertValToIdUser_Credit` functions                                                                                                      |

#### < dateDB.py >
This file is responsible for creating/updating the credit tables for the credit databases. 

The three credit date databases are: 

**groupName_creditcarddate**: Contains information on when the statement generates for all the credit cards that every user of the group has

**groupName_otherdate**: Contains information on when the statement generates for all the other credit cards/products that every user of the group has

| Functions | Description                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| `dateDetails(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)`    | This function will collect details on your when your statement generates for all your credit sources |
| `getCreditInfoFromDict(val_tableName, val_userName, dict, type)`    | This function extracts all the credit data from the tables and outputs them as a list of tuples      |
| `createTable(val_tableName, val_userName, dict, type)`    | This function will call the `creditTableDB()` and `insertValToIdUser_Credit` functions               |
| `MapVal(val_tableName, val_userName, dict, type)`    | This functions is responsible for inserting values into the credit tables                            |


#### < report.py >
This file is responsible for creating the `report.txt` file that will have information on the **Spending Limit** and **General Re-Payment Date**

| Functions                                                                                                       | Description                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `reportGenerate(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)`          | This function is the main function that is responsible for creating the report                                |
| `generateHeader(val_userName, val_tableName)`                                                                   | This function is responsible for creating the title/header details in the report                              |
| `printMainDB(val_tableName, val_userName)` <br/> getCreditInfo(val_tableName, val_userName, dict, type) <br/>  getCreditHeadersInDB(val_tableName, type) | These functions are responsible for retrieving data/header information from the credit tables in the database |
| `convertTupToStringMod(dict)`                                                                                                          | This function converts the input dictionary from tuples to a list of strings                                  |
| `printValBesideHeader(val_userName, credit_header_info, credit_dbinfo, type)`                                                                                                          | This function will allow the headers and values to be printed side by side in the main report                 |

## <ins> Product Usage
When you boot up the product, you will be prompted with the following 5 responses.

    Please choose from the following options:
        (1) Is this your first time running this program --> Type 1
        (2) Add user to database --> Type 2 
        (3) Configure bill payments --> Type 3 
        (4) Configure credit limits --> Type 4  
        (5) Get updated report --> Type 5
        Choice = 

*Please find your report.txt file from option (5) in the directory that you ran your script from*

The goal is to publish this product in an .exe format and eventually as a web application. The web application would make
the product more user-friendly and allow for easier distribution.

## <ins> Testing
A simple trial/error testing method was implemented during the development of this product, however, Unit Testing is yet to be implemented. 

A thorough analysis will be done to see if the product works as intended in version 2 release.

## <ins> Improvements
For version 2 release, the following improvements will be made:
- Test the product thoroughly 
- Add feature for secondary user to add their credit information
- Complete feature for users to update their credit information
- Complete feature for users to configure their bill payments
