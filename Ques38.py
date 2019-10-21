# Create 2 dictionaries as follows;
# dict1 ={'Name':'Ramakrishna','Age':25}
# dict2={'EmpId':1234,'Salary':5000}
# Perform following operations
# a) Create single dictionary by merging dict1 and dict2
# b) Update the salary to 10%
# c) Update the age to 26
# d) Insert the new element with key "grade" and assign value as "B1"
# e) Extract and print all values and keys separately.
# f) delete the element with key 'Age' and print dictionary elements.

def Merge(dict1, dict2):
    return(dict1.update(dict2))


dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}

# a) Create single dictionary by merging dict1 and dict2
Merge(dict1,dict2)
print(dict1)


# dict = str(dict1)+str(dict2)
# print(dict)

# b) Update the salary to 10%
dict2["Salary"]=5500
print(dict2)

# c) Update the age to 26
dict1["Age"]= 26
print(dict1)

# d) Insert the new element with key "grade" and assign value as "B1"
dict1["Grade"]="B1"
print(dict1)

# e) Extract and print all values and keys separately.
print(dict1.keys())
print(dict1.values())
print(dict2.keys())
print(dict2.values())

# f) delete the element with key 'Age' and print dictionary elements.
del dict1["Age"]
print(dict1)