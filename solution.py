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
fulltime_df = pd.merge(employee_df, salary_df, on='name').where(employee_df['type'] == 'full_time').where(employee_df['seniority'] > 12).dropna()
# nice :D
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

#create dictionary to map employees to their children, rather than to their parent
children_dict = {}
for index, row in fulltime_df.iterrows():
    # if the supervisor isn't in the dict yet
    if row['reports_to'] not in children_dict:
        # if this item is the CEO, we don't want to include it's name in its children
        if row['name'] not in row['reports_to']:
            children_dict[row['reports_to']] = [(row['name'])]
    # supervisor is already in the dict, so we append its list instead of overwriting/creating a new one
    else:
        children_dict[row['reports_to']].append(row['name'])
    # if the current employee supervises isn't in the dict yet, add them with an empty list
    if row['name'] not in children_dict:
        children_dict[row['name']] = []

class Employee(object):
    #a list of tuples
    EXPENSES = []

    def __init__(self, name, children_dict, fulltime_df):
        #name/key of employee object
        self.name = name
        #name of the company CEO
        self.ceo = fulltime_df.loc[fulltime_df['name'] == fulltime_df['reports_to']].iloc[0]['name']
        #list of children filled with employee objects
        self.children = self.get_children(children_dict[self.name], children_dict, fulltime_df)
        #data
        self.seniority = fulltime_df.where(fulltime_df['name'] == self.name).dropna().iloc[0]['seniority']
        self.salary = fulltime_df.where(fulltime_df['name'] == self.name).dropna().iloc[0]['salary']
        self._type = fulltime_df.where(fulltime_df['name'] == self.name).dropna().iloc[0]['type']
        #print(str(self.name)+' '+str(self.seniority)+' '+str(self.salary)+' '+str(self._type))
        pass

    def get_children(self, children, children_dict, fulltime_df):
        #method for finding this employees children using the children_dict created in main
        temp = []
        # base case: The employee has no children -> return an empty list
        if(children == []):
            return []
        else:
            # for each name in the children list, create a new employee and append it to the temp list. Then return the temp list (a list of employee objects)
            for i in children:
                temp.append(Employee(i, children_dict, fulltime_df))
            return temp
        pass

    def get_expenses(self, sum=0):
        #method for recursively getting the expenses of this employee and all its children. stores this data in EXPENSES (local dict)
        #uses print expenses to print out a table of the EXPENSES dict
        if(self.children == []):
            #print(self.name + str(self.salary))
            #if no children, add this employees salary to the table and return self.salary for calculation of parent expenses
            self.add_expenses(self.salary)
            return self.salary
        else:
            #if children exist, call this function on each child, storing their expenses in sum
            for i in self.children:
                sum += i.get_expenses(sum)
            
            #print(self.name + str(sum))
            #once all children expenses have been added to sum, add self.salary to sum and add that value to EXPENSES table
            #call the print_exp_table function to print the EXPENSES dict as a pd.DF
            #then return self.salary + sum for calculation of parent expenses
            self.add_expenses(sum + self.salary)
            self.print_exp_table()
            return sum + self.salary
        pass

    def add_expenses(self, exp):
        #method to add employees and their expenses to the EXPENSES list
        #step 3 solution
        #self.EXPENSES.insert(0, (self.name, exp) )
        
        #step 5 solution
        self.EXPENSES.insert(0, (self.name, exp, self.seniority) )
        pass

    def print_exp_table(self):
        #method to print EXPENSES dict as a DF table
        #we only want to print out the CEO's table (unordered) as this contains data for the whole company, rather than all sub-tree tables.
        ##################################
        #   Step 3 Solution
        #if(self.name == self.ceo):
        #    print("\nRecursive Step-3 Solution:")
        #    print(pd.DataFrame(self.EXPENSES, columns=['Employee', 'Expenses']))
        #    pass
        ##################################

        ##################################
        #   Step 5 Solution
        if(self.name == self.ceo):
            print("\nRecursive Step-5 Solution:")
            print(pd.DataFrame(self.EXPENSES, columns=['Employee', 'Expenses', 'Seniority']))
            pass
        ##################################
        
# Step 2b: Create the company tree from the fulltime_df dataframe. The 'company' variable must be set to the root of the tree (the CEO Steve Jobs). If you're feeling confident, attempt this solution recursively (pass the entire fulltime_df dataframe to the class constructor or a class method).

#determine the CEO of the company, which is the employee who reports to themselves
ceo = fulltime_df.loc[fulltime_df['name'] == fulltime_df['reports_to']]
#create the company tree, passing in the CEO name to be the root. children_dict is passed to help recursively build the tree
company = Employee(ceo.iloc[0]['name'], children_dict, fulltime_df)
    
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
    #method to iteratively traverse the tree and determine the expense for each employee
    #expenses_dict to keep track of the running count for each node, since I can't alter the Employee class to include this variable
    expenses_dict = {}
    #stacks to help traverse the tree iteratively
    stack1 = []
    stack2 = []

    #initialize stack1 to contain the root
    stack1.append(employee)

    #use stack1 to comb through the tree, adding nodes in order of visit to stack 2
    while stack1:
        visit = stack1.pop()

        #initialize employee's expenses to their own salary
        expenses_dict[visit.name] = visit.salary
        stack2.append(visit)
        for child in visit.children:
            stack1.append(child)

    while stack2:
        visit = stack2.pop()

        # if visiting node has children, add childrens expenses to visiting nodes expenses
        # if no children, nothing happense as we already initialized their expenses in the first while loop
        if(len(visit.children) > 0):
            for child in visit.children:
                expenses_dict[visit.name] += expenses_dict[child.name]

    #convert expenses_dict to a pretty Pandas DF and print it
    print("\nIterative Solution:")
    print(pd.DataFrame(expenses_dict.items(), columns=['Employee', 'Expenses']))
    pass

# Step 6: Test it
# Expected:
# Steve Jobs     |    4.0
# Bill Gates     |    1.5
# Steve Balmer   |    0.5
# Warren Buffett |    1.0

get_expenses_iterative(company)

# Have a great day!
