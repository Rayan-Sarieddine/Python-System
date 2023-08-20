import datetime
employees={}

#read employees line by line from users.txt file
def readEmployees(employees):#time complexity=O(n) where n= number of lines in the users file
    with open("users.txt", "r") as f: #https://www.w3schools.com/python/python_file_open.asp
      for x in f:
          line=x.split(",")
          employees[line[0].strip().lower()]={
          "username":line[1].strip().lower(),
          "timeStamp":int(line[2].strip()),
          "gender":line[3].strip().lower(),
          "salary":float(line[4].strip())
        }
          

#display number of male and female employees registered in the system
def statistics(employees):# time complexity: O(n) where n= number of employees (i.e number of lines in the users file)
    countMale=0
    countFemale=0
    for emp in employees.values():
        if emp['gender'] == 'male':
            countMale=+1
        elif emp['gender'] == 'female':
           countFemale+=1
    return f"there are {countFemale} female employees and {countMale} male employees"


#add a new employee to the empolyees dictionary
def addEmployee(employees):# time complexity: O(1) fixed time for adding 1 employee at a time
    username = input("Enter Username: ")
    gender = input("Enter Gender (male/female): ")
    while gender!="male" and gender!="female":
       gender = input("please enter correct gender (male/female): ")
    salary = int(input("Enter salary: "))
    while salary<0:
       salary = int(input("Please enter correct salary: "))
    length=len(employees)
    if length<9:
       id="emp00"+str(length+1)
    elif length>8 and length<99:
       id="emp0"+str(length+1)
    else:
       id="emp"+str(length+1)
    today = datetime.datetime.today().strftime("%Y%m%d")
    employees[id]={
       "username":username,
            "timeStamp":int(today),
            "gender":gender,
            "salary":int(salary)
       
    }
    print("Successfully added!")

#def displayAll(employees):


#change the salary of an employee that exists
def salaryChange(employees): #time complexity: O(1) considering we are changing the salary of 1 employee at a time and the dictionary look has also a fixed time complexity of O(1)
  id=input("Enter employee ID: ")
  if id in employees:
    salary=int(input("Enter new salary: "))
    while salary<0:
      salary = int(input("Please enter correct salary: "))
    employees[id]["salary"]=salary
    print("The salary is changed")
  else:
    print("Employee not found")