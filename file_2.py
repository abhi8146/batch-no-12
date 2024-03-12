'''
temp=a #temp=7
a=b  #a=5
b=temp #b=7

# # a=5, b=7
# print(a,b)

# Eg:2
 a=a+b #a=12
 #b=a-b #b=12-7=5
 #a=a-b #12-5=7

 # print(a,b)

 #a, b=b, a # only in python
 # print(a, b)

 a=a*b #a=35
 b=a/b #b=35/7=5.0
 a=a/b #a=35/5=7.0
 print(int(a),int(b))

 # id()--> used to find the memory address of the variable
 a=7
 b=8
 # print(id(a))
 # print(id(b))

 # ---> keywords
 # keywords are reserved words which provides secial meaning to
 # compiler or interpretor
'''
'''
import keywords
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

# to check if the string is keyword or not
# print(keyword.iskeyword("abhi"))#false

# if = 8 `
# !--->literals
# literals is the constant valve assigned to a variable
# A variable is considers to be constant when it is defines
# in caps

# a= 78 # a is variable
# A=78 # A is constant

l1=[6,7,8,0]


# hash()---> it creats a hash valve for constant datatype and
# provides error for non constant datatype 
n1 = 89+7j
print(hash(n1))

f1 = [7,8,9]
print(hash(f1))# error ---> list is non-constant or mutable datatype

# a= 9
# b= 9
# b= 90
# print(id(a))
# print(id(a))

#! ----> operators
 ==> operators are symbols which is used to perform various operions
 ==> between 2 or more operands

 # Arithmatic
 # Assignment
 # Logical
 # Relational or comparison
 # Bitwise
 # Identity
 # Membership

 # too----> Arthmatic --> +,-,*,/,//,**
 # Eg:1
 # a=8
 # b=6
 # c=9
 # print(a+b+c)

 # input()---> used to get the runtime input
 # n1m = input("enter the valve:")
 # print(type(n1))


 # eval()---> used to get the runtime valves of all datatype
 # n1 = eval(input("enter the valve:"))
 # print(type(n1))

 # a =4
 # b =2
 # print(a/b) # is used to get the quotient valve
 # print(a%b) # is used to get the remainder valve


 # ! // --> floor devision

 # a =765433
 # b =19
 # print(a//b) #--> the output will be inn integer & the output will be
 # based on the floor valve

 #! ** --> used for power of a number
 # print(2**4) # --->16

 # ! Assignment --->+-=, -=, /=, *=, //=, **=, &-, |=, %=
 # a=8
 # a+=2
 # print(a)

 # a=30
 # a-=5
 # print(a)


 # ! comparison--> ==, >, <, |=, <=, >=
 # a=8
 # b=7
 # print(a>b) # true

 # a=9
 # b=5
 # print(a==b)

 # ! bitwise operator ---> &, |, ^, ~, <<,>>
 a = 7
 b = 4
 print(a|b)

 # 2^4  2^3  2^2  2^1  2^0
 #  8    4    2     1

 #  0     1    1     1   #--->7
 #  0     1    0     0   #--->4&
 #  ------------------------
 #   0     1    0     0
 
 # ~ ---->
 # a = 9876
 # print(~a)


 # a = 9

 # 128 64 32 16 8 4 2 1
 #  0   0  0  0 1 0 0 1 #--->  9

 #  1   1  1  1 0 1 1 0 # --->  -10

 #  0  0   0  0 1 0 1 0 --->  10

 #  1  1   1  0  1  0  1 ---> is compliment of 10
                    #  1 ---> 2s compliment
  # ---------------------------------
  # 1  1  1  1  0  1  1  0 --->  -10

  # 256 128 64 32 16 8 4 2 1
  #   0   0  0  0  0 0 1 0 1
  #   0   0  0  1  0 1 0 0 0 --->  40
  # 107

  # <<, >>
  # print(5>>1)
  # 16>4

  # ! Logical ---> used to compare the expressions
  # and, or , not
    a = 6
  # print(a>3 and a<10)
  # print(a>7 or a<30)
  # print(not(a>8 and a<10)

  #! Identity operator
  # ? it is used to compare the memory location that the valve
  # ? are stored
  
  # Is, is not
  a = 8
  b = 8
  print(a is b)
  print(a==b)

  a = [1, 2, 3]
  b = [1, 2, 3]
  print(a is not b)

# ! MERMBERSHIP OPERATOR
# in, not in
l1 = [7,8,9,0,6,5]
# num = 55
# print(num in l1)
# print(num not in l1)

num = 678
# print(8 in num) # error

# ! CONDITIONAL STATEMENT
# if, elif, else


#{
# phyton syntax
# if condition:
#    statement
#    statement
#    statement
# statement

# eg:1
# a = 6
# if a:
#     print("hello")

# Eg:2
# a = 6
# if a>3:
#    print("hey")
# else:
#    print("no")


# Eg:3
# if 7>8:
#      print("hello")

# print("no")


# Eg:4
# a = 0
# a = none
# a = false
# a=""
# if a:
#   | print("yes")
# else:
#     print("no")


# a number is even or odd
# n = int(input("enter the number:"))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")
'''
name=input("enter name:")
age=int(input("enter age:"))

