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

__Targeted User:__ The product will be really useful for people with low to no credit or people that just want to increase their score in general.
The two major features of this product would one allow the user to condition themselves a new spending limit based on the 
recommended 30% limit in each credit product and two have a general day in each month that they user should remember to pay 
off statement balances for all their credit products.

__Technologies:__
> <span style = "color:green"> Git | Python | Unit Testing | PostgreSQL </span>

## <ins> Design
### Project Architecture

![my image](./assets/architecture.png)

#### Register Checkout System
The Register Checkout System will assist with finding the total cost of all the items in a customer’s cart, including taxes.

| Functions | Description |
|-----------|-------------|
| `name`    | Description |
| `name`    | Description |

#### Inventory Management System
The Inventory Management System can be used to keep a track of how much items we have of a certain product as well as add/remove items from the inventory.

| Functions | Description |
|-----------|-------------|
| `name`    | Description |
| `name`    | Description |


## <ins> Product Usage
When you boot up the product, you will be prompted with the following 5 responses.


    Please choose from the following options:
        (1) Is this your first time running this program --> Type 1
        (2) Add user to database --> Type 2 
        (3) Configure bill payments --> Type 3 
        (4) Configure credit limits --> Type 4  
        (5) Get updated report --> Type 5
        Choice = 

The goal is to publish this product in an .exe format and eventually as a web application. The web application would make
the product more user-friendly and allow for easier distribution.


## <ins> Testing
A simple trial/error testing method was implemented during the development of this product, however, Unit Testing is yet to be implemented. 
A thorough analysis will be done to see if the product works as intended in version 2 release.

#### Register Checkout System

![my image](./assets/checkout_counter_test.png)

#### Inventory Management System

![my image](./assets/inventory_managment_test.png)

## <ins> Improvements
For version 2 release, the following improvements will be made:
- Test the product thoroughly 
- Add feature for secondary user to add their credit information
- Complete feature for users to update their credit information
- Complete feature for users to configure their bill payments
