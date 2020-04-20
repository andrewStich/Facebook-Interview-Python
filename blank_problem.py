import pandas as pd

# Thank you for interviewing! This should take approximately 1 hour of your time; you may use up to 3 if necessary. 

#Feel free to call ********** for 15 minutes of help. Please pay attention to code quality, use 'Pythonic' coding style when possible, and comment like you normally would. Use any documentation that you need.

# Do not modify below this line
employee_db = {'name':['Steve Wozniak', 'Morgan Stanley', 'Steve Jobs', 'Bill Gates', 'Steve Ballmer', 'Warren Buffett', "Intern McIntern"], 'reports_to': ['Steve Jobs', 'Bill Gates', 'Steve Jobs', 'Steve Jobs', 'Bill Gates', 'Steve Jobs', 'Warren Buffett'], 'seniority':[30, 45, 24, 28, 20, 13, 9], 'type': ["hourly","hourly","full_time","full_time","full_time","full_time", "full_time"]} 
salary_db = {'name':[ 'Bill Gates', 'Steve Ballmer', 'Warren Buffett', "Intern McIntern", 'Steve Wozniak', 'Morgan Stanley', 'Steve Jobs'], 'salary':[1, 0.5, 1, 0.1, 0.25, 0.33, 1.5]}

employee_df = pd.DataFrame(employee_db)
salary_df = pd.DataFrame(salary_db)

print(employee_df)
print(salary_df)
# Do not modify above this line

# Step 1:
# Using the dataframes 'employee_df' and 'salary_df', create a new dataframe 'fulltime_df' that contains salary, seniority, type, and reports_to columns. Filter this dataframe to contain only employees that are full time and have been with the company longer than 1 year. Use this filtered dataframe in the rest of this exercise. 

# "salary" is in units of millions
# "seniority" is in units of months
# Expected answer:
#              name      reports_to  seniority       type  salary
#1       Steve Jobs      Steve Jobs         24  full_time    1.50
#2       Bill Gates      Steve Jobs         28  full_time    1.00
#3    Steve Ballmer      Bill Gates         20  full_time    0.50
#4   Warren Buffett      Steve Jobs         13  full_time    1.00

pass

# Step 2a: 
# Complete this Employee class definition. This class should implement a tree. This is not a binary tree; please support many employees per manager. 
# Example:
#
#                             Steve Jobs (salary 1.5M$)
#                            /                     \
#                 Bill Gates (salary 1M)       Warren Buffett (salary 1M) 
#                        /  
#            Steve Ballmer (salary 0.5M)   
#            
# get_expenses() must return the salary of the current employee, plus salaries of all reports, recursively. 
#
# Example: billGatesInstance.get_expenses()
#          > 1.5M
# You may add or modify any methods and class variables inside this class, but all your work must be done entirely within class Employee(). 

class Employee(object):
    
    def __init__(self):
        pass

    def get_expenses(self):
        pass

        
# Step 2b: Create the company tree from the fulltime_df dataframe. The 'company' variable must be set to the root of the tree (the CEO Steve Jobs). If you're feeling confident, attempt this solution recursively (pass the entire fulltime_df dataframe to the class constructor or a class method).


company = Employee()
    
# Step 3: Print the expenses for every employee as a table. Ex: 
# Employee       |   Expenses   
# Steve Jobs     |    4.0
# Bill Gates     |    1.5
# Steve Balmer   |    0.5
# Warren Buffett |    1.0

company.get_expenses()

# Step 5: Modify the class to report the seniority of each employee. Modify the class in Step 2a to print this in a table that looks like this:
# Expected:          Salary    Seniority
# Steve Jobs     |    4.0   |   24
# Bill Gates     |    1.5   |   28
# Steve Balmer   |    0.5   |   20
# Warren Buffett |    1.0   |   13

pass

# Step 4: Implement the get_expenses_iterative() method
# This method does the exact same thing as your previous solution, but you must implement it within just this function below. All your work must be within the function. You may not modify the function arguments. Do not use the recursive get_expenses() method in this solution.

def get_expenses_iterative(employee):
    pass

# Step 6: Test it
# Expected:
# Steve Jobs     |    4.0
# Bill Gates     |    1.5
# Steve Balmer   |    0.5
# Warren Buffett |    1.0

get_expenses_iterative(company)

# Have a great day!
