employeeName = input("Type an Employee Name ( Jack or Fei ) :")

employee = {
    "Jack": {
        "Birthday" : "June 6 , 1998",
        "SSN" : " 324439864863",
        "Education" : "Some College credits"
    },

    "Fei": {
        "Birthday" : "June 1 , 2003",
        "SSN" : "81278948940134",
        "Education" : "High School"
    }

}

employeeString = " "
if employeeName in employee:
    employeeString += str(employee.get(employeeName, " "))

print(employeeString)