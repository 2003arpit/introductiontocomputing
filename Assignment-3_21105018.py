#QUESTION-1

print("\n                    QUESTION-1\n")

#Initializing null lists
list1=[]
list2=[]
list3=[]



#Defining function for counting character of a single word
def count_character(str):
    list1=list(str)

#Making unique list of characters of input word

    for item in list1:
        if item not in list2:
            list2.append(item)

#Printing occurance of characters in the input word
    for i in range(0,len(list2)):
        print("Number of occurance of ",list2[i],": ",str.count(list2[i]))

#Defining function for counting words in the input string

def count_word(str):
    word=lower_input_string.split()


#Making list of unique characters
    for item in word:

        if item not in list3:
            list3.append(item)


#Printing occurance of words in input string
    for q in range(0,len(list3)):
        print("Number of occurance of",list3[q],": ",str.count(list3[q]))


#Taking string as input from user
input_string=str(input("Enter your string:\n"))
lower_input_string=input_string.lower()

words_count=len(lower_input_string.split())

#Using different function for a single word or string
if words_count==1:
    count_character(lower_input_string)
else:
    count_word(lower_input_string)

# QUESTION-2

print("\n                QUESTION-2\n")

# Taking input from user
year = int(input("Input a year: "))

# condition for loop year
if (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# taking input month
month = int(input("Input a month [1-12]: "))

# for months of 31 days
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31

# for february month
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28

# for months of 30 days
else:
    month_length = 30

# taking input day
day = int(input("Input a day [1-31]: "))

# warning for wrong inputs
if day > month_length:
    print("invalid input.")

elif day < month_length:
    day += 1
    print("The next date is %d/%d/%d." % (day, month, year))

else:
    day = 1
    if month == 12:
        month = 1
        year += 1
        print("The next date is %d-%d-%d." % (day, month, year))

    else:
        month += 1

    # printing output
    print("The next date is %d-%d-%d." % (day, month, year))

#QUESTION-3

print("\n                    QUESTION-3\n")

#Initializing null lists
list1=[]
list2=[]

#Taking a list as input from user

list1=list(map(int,input("Enter numbers seperated by space:\n").split()))

# #Squaring numbers and appending them in list2
for i in range(0,len(list1)):

    square=(list1[i],list1[i]**2)
    list2.append(square)
    i=i+1

#printing list2
print("\nRequired list is:\n",list2)


#QUESTION-4

print("\n                  QUESTION-4\n")

#Taking grade as input from user
input_grade=int(input("Enter you grade between 4 to 10:\n"))

# Making list of performance remarks
list1=["Outstanding","Excellent","Very Good","Good","Average","Below Average","Poor"]

# Making list of grades
list2=["'A+'","'A'","'B+'","'B'","'C+'","'C'","'D'"]

#limits on grades
if input_grade>10 or input_grade<4:
    print("Invalid Input")
else:
    #Printing respective grade and remark
    print("Your Grade is",list2[10-input_grade],"and",list1[10-input_grade],"Performance.")



#QUESTION-5

print("\n                  QUESTION-5\n")

rows_number = 6

#loop for number of rows

print("Required pattern:\n")
for i in range(rows_number):

    # printing spaces
    for j in range(i):
        print(" ", end="")

    # printing alphabet
    for j in range(2*(rows_number-i)-1):
        print(chr(65 + j), end="")
    print()


#QUESTION-6

print("\n                    QUESTION-6\n")

#Initializing a null dictionary
dictionary={}
dictionary2={}
dictionary3={}
dictionary4={}

#running an infinite while loop with a condition
while(1):

    input_condition = str(input("Do you want to enter student name and SID\nIf yes press 'Y' or'y' if no press 'N' or 'n':\n"))

    if input_condition=="Y" or input_condition=="y":
        input_sid=int(input("\nEnter the SID of student:\n"))
        input_name=str(input("\nEnter the name of student:\n"))
        if input_sid<0:
            print("\nSID can't be negative\n")
        else:
            dictionary.update({input_sid: input_name})
            dictionary2.update({input_name:input_sid})

    elif input_condition=="N" or input_condition=="n":
        break
    else:
        print("\nInvalid input\n")

print("\n                   QUESTION-6(a)\n")

#Printing Dictionary

print("\nRequired dictionary:\n",dictionary)


print("\n                  QUESTION-6(b)\n")

list=sorted(dictionary2)

for item in list:
    dictionary3.update(({dictionary2.get(item): item}))

print("\nDictionary after sorting according to name:\n",dictionary3)

print("\n                   QUESTION-6(c)\n")

#Sorting on the basis of key
list2=sorted(dictionary)

for item in list2:
    dictionary4.update({item:dictionary.get(item)})
print("\nDictionary after sorting according to SID\n",dictionary4)

print("\n                  QUESTION-6(d)\n")

#Search student with SID
input_search=int(input("\nEnter the SID of the student:\n"))
print("\nName of the student with SID",input_search,"is:\n",dictionary[input_search])



#QUESTION-7

print("\n               QUESTION-7\n")

#Defining function for fibonacci series

def fibonacci(n):
    if n==1 :
        return 0
    if n==2:
        return 1

    elif n<=0:
        return print("incorrect input")

    else:
        return fibonacci(n-1)+fibonacci(n-2)

#Defining average function for fibonacci numbers
def average(list):
    return sum(list)/len(list)

#Taking input from user

var1=int(input("enter the number of fibonacci series terms you want to print:\n"))

#Initializing a null list
list1=[]

#Loop to append elements in list

print("Required Fibbonacci series:")
for i in range(1,var1+1):
    
    #Printing fibonacci series
    print(fibonacci(i),end=" ")
    list1.append((fibonacci(i)))

#Printing average
print("\n\nAverage of first", var1 ,"numbers of fibonacci series :\n",average(list1))


#QUESTION-8

print("\n                QUESTION-8\n")

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

print("\n               QUESTION-8(a)\n")

#Union of set1 and set2

set4=set1.union(set2)

#Intersaction of set1 and set2

set5=set1.intersection((set2))

print("\nSet containing all elements of Set1 and Set2 but not both:\n",set4-set5)

print("\n                QUESTION-8(b)\n")

set6=set1-set2-set3
set7=set2-set3-set1
set8=set3-set2-set1
set9=set6.union(set7).union(set8)

print("\nSet containing elements that are on;y in one of the three sets Set1,Set2,Set3:\n",sorted(set9))


print("\n                QUESTION-8(c)\n")

set11=set2.intersection(set3)
set12=set5.union(set11)
set14=set1.intersection(set3)
set13=set12.union(set14)
set15=set5.intersection(set3)
set_c=set13-set15

print("\nSet of elements that are exactly two of the given sets:\n",set_c)


print("\n                QUESTION-8(d)\n")

set10=set()
for i in range(1,11):
    set10.add(i)
    i+=1

print("\nSet of all integers from 1 to 10 that are not in set1:\n",set10-set1)


print("\n                QUESTION-8(e)\n")
print("\nSet of all integers from 1 to 10 that are not in set1,set2,set3:\n",set10-set1-set2-set3)
