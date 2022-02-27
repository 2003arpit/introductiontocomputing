# QUESTION - 1

print("\n                         QUESTION - 1\n")

# Defining tower of Hanoi function

def hanoi_tower(n , start, finish, auxiliary):



    if n==1:

        print ("\nMove disk 1 from ",start,"to",finish,"\n")
        return

    hanoi_tower(n-1, start, auxiliary, finish)

    print ("\nMove disk",n,"from",start,"to",finish,"\n")

    hanoi_tower(n-1, auxiliary, finish, start)


# taking number of disk input from the user

no_of_disk=int(input("Enter number of disk in tower of Hanoi:\n"))

# Using the function of hanoi tower

hanoi_tower(no_of_disk,"Source Tower","Destination","Auxiliary")




# QUESTION - 2

print("\n                        QUESTION - 2\n                  using RECURSIVE approach")

n = int(input("Enter the number of rows : \n"))

def pascalstriangle(num):

    if num == 1:
        return [[1]]

    else:

        result = pascalstriangle(num-1)
        present_row = [1]
        previous_row = result[-1]

        for i in range(len(previous_row)-1):

            present_row.append(previous_row[i] + previous_row[i+1])

        present_row += [1]

        result.append(present_row)
    return result

for i in pascalstriangle(n):

    print((n-len(i))*"  ", end=" ")

    for j in i:

        print(j, end="   ")
    print()




print("\n                        QUESTION - 2\n                  using ITERATIVE approach")


#number of rows
n=int(input("Enter the number of rows:\n"))

for p in range(1, n+1):

    print('  '*(n - p), end='')

    x = 1
    for i in range(1, p+1):

        print(x, end='   ')

        x = x * (p - i) // i
    print()
print("")



 # QUESTION - 3

print("\n                         QUESTION - 3\n")


# Taking input

n1=int(input("\nEnter an Integer : \n"))

n2=int(input("Enter another Integer : \n"))

#Making a list of return values

list1 = list(divmod(n1, n2))

# a1 = Quotient

q = list1[0]

# a2 = Remainder

r = list1[1]

# printing the quotient and remainder

print(f"\nThe quotient when {n1} is divided by {n2} is {q}.\n")
print(f"\nThe remainder when {n1} is divided by {n2} is {r}.\n")


# QUESTION - 3(a)

print("\n                         Que3(a)\n")

c1 = callable(divmod(n1, n2))
if c1 == True:
    print(f"Function is callable")

if c1 == False:

    print(f"Function is Not-callable")


# QUESTION - 3(a)

print("\n                         Que3(B)\n")

#list of values

list1 = [q, r]
zero = False
if zero in list1:
    zero = True
else:
    zero = False
if zero == True:

    print("All result values are NOT 'non-zero'")
elif zero == False:

    print("All result values are 'non-zero'")

#QUESTION -3(C)


print("\n                         Que3(C)\n")

#new values of list

list2 = [q, r]

for i in range (4, 7):

    list2.append(i)

print(f"Appended (4,5,6) in the values ({q},{r})")

listv2 = []

# adding number > 4 from listr to listv2

for i in list2:
    if i > 4:
        listv2.append(i)
# a new list listv3 with same elements as listv2 but in string form

listv3 = list(map(str, listv2))

# Using join

v = ",".join(listv3)

print(f"Values greater than 4 is {v}")


# QUESTION- 3(D)
print("\n                         Que3(D)")

set1 = {1, 2}
set1.clear()

# adding above result in set datatype

for P in listv2:
    set1.add(P)

print("Above result in set form is shown below:\n")

print(set1)


#QUESTION - 3(E)
print("\n                         Que3(E)")

#Making set1 immutable

frozenset(set1)

print("The above set has been converted to immutable.")

#QUESTION - 3(F)

print("\n                         Que3(F)")

print(f"Max value from set is {max(set1)}")

#using hash function

hash_value = hash(max(set1))

print(f"Hash value of {max(set1)} is {hash_value}")

# QUESTION - 4

print("\n                         QUESTION - 4\n")

# making a class

class student:

    #using constructor to create class objects

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    #defining print function

    def print(self):

        print(f"Hello, My name is {self.name} and my "
              f"sid is {self.sid}")

    #calling destructor

    def __del__(self):
        print("Object Destroyed")

# making an object of student class

arpit = student("Arpit", 21105018)
arpit.print()
del arpit



# QUESTION - 5
print("\n                         QUESTION - 5\n")

#making an employee class

class employee :

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# creating employee records

employee1 = employee("Mehak", 40000)
employee2 = employee("Ashok", 50000)
employee3 = employee("Viren", 60000)

print("\n                         Part(a)\n")

employee1.salary = 70000

print(f" Salary of {employee1.name} after update is {employee1.salary}")

print("\n                         Part(b)\n")


del employee3
print("Employee Viren's data has been removed.")



# QUESTION - 6

print("\n                         QUESTION - 6\n")


print( "\n                 WELCOME TO THE FRIENDSHIP GAME\n" )

# defining game function

def game(word1,word2):

    #all letters to lowercase

    word1 = word1.lower()
    word2 = word2.lower()

    #initialising empty lists to store alphabets

    list1=[]
    list2=[]

    for i in word1:
        list1.append(i)
    for p in word2:
        list2.append(p)

    #sorting the list alphabetically

    list1.sort()
    list2.sort()

    #condition for friendship

    if list1==list2:

        return True
    else:
        return False

#taking players name input

player1=str("Barbie")

player2 = str("George")

#taking words spoken by written

word_player1 = str(input(f"\nEnter Word by {player1} : \n"))

word_player2 = str(input(f"\nEnter Word by {player2} : \n"))

#using game function

result=game(word_player1,word_player2)

#printing the final result

if result == True:

    print(f"\n{player1} and {player2} are real friends!")

elif result == False :

    print(f"\n{player1} and {player2} are fake friends!")

