 #QUESTION 1

print("                   QUESTION 1(a)")

#giving value to string_1
string_1=str("Python is a case sensitive language")

#printing length of string_1
print("Length of the string is:\n",len(string_1))

print("                   QUESTION 1(b)")

#printing string_1 in reverse order
print("String in reverse order :\n",string_1[::-1])

print("                   QUESTION 1(c)")

#slicing string_1
string_new=string_1[10:26]

#printing string_new
print(string_new)

print("                   QUESTION 1(d)")

#making replacement in string
x=string_1.replace("a case sensitive","object oriented")

#printing new string
print("String after replacement:\n",x)

print("                   QUESTION 1(e)")

#printing index of "a" in string_1
print("Index of 'a' in given string:\n",string_1.index("a"))

print("                   QUESTION 1(f)")

#making replacement in string_1 and printing it
print("String after removing white spaces:\n",x.replace(" ",""))

# QUESTION 2

print("                   QUESTION 2")

#initilising variables
name=str("Arpit Singhal")
sid=int(21105018)
department=str("electronic and communication engineering")
cgpa=float(9.9)

#printing required details
print("Hey,%s"%(name),"Here!\nMy SID is %s"%(sid),"\nI am from %s"%(department),"and my CGPA is %s"%(cgpa))



# QUESTION 3

print("                   QUESTION 3(a)")

#initialising a and b
a=56
b=10

#printing a&b
print("a&b is\n",a&b)

print("                   QUESTION 3(b)")

#printing a|b
print("a|b is\n",a|b)

print("                   QUESTION 3(c)")

#printing a^b
print("a^b is\n",a^b)

print("                   QUESTION 3(d)")

#left shift both a and b by 2 bits
print("Shifting a by 2 bits left we get:\n",a<<2)
print("Shifting b by 2 bits left we get:\n",b<<2)

print("                   QUESTION 3(e)")

#right shift a by 2  its and left shift b by 4 bits
print("Shifting a by 2 bits right we get:\n",a>>2)
print("Shifting b by 4 bits right we get:\n",b>>4)



# QUESTION 4

print("                   QUESTION 4")

#taking numbers as inputs
number_1=float(input("Enter first number:\n"))
number_2=float(input("Enter second number:\n"))
number_3=float(input("Enter third number:\n"))

#finding highest number
if number_3>number_2 and number_3>number_1:
    print("The greatest number is:\n",number_3)
if number_1>number_3 and number_1>number_2:
    print("The greatest number is:\n",number_1)
if number_2>number_3 and number_2>number_1:
    print("The greatest number is:\n",number_2)

# QUESTION 5

print("                   QUESTION 5")

#taking input string from user
string_2=str(input("Enter the string:\n"))

#finding name is string_2
if str("name") in string_2:
    print("Yes")
else:
    print("No")

# QUESTION 6

print("                  QUESTION 6")

#taking length of 3 sides as input from user
side_1=float(input("Enter the length of first side:\n"))
side_2=float(input("Enter the length of second side:\n"))
side_3=float(input("Enter the length of third side:\n"))

#checking condition for trinagle
if side_1+side_2>side_3 and side_1+side_3>side_2 and side_3+side_2>side_1:
    print("Yes")
else:
    print("No")
