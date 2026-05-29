# write a python program to decalare varables of different data types such as:
# integer, float, string, Boolean    
# print their value and data type


# int=25
# float=10.4
# string="rehan"
# bol=True

# print("int value :- ",int)
# print("type of value :- ",type(int))

# print("float value :- ",float)
# print("type of value :- ",type(float))

# print("string value :- ",string)
# print("type of value :- ",type(string))

# print("Boolean value :- ",bol)
# print("type of value :- ",type(bol))



# create a string variable with you name and perform the following
# convert it to uppercase
# convert it to lower case
# find the length of the string
# replace on character with another

# str="i am a boy"

# print("my string :- ",str)

# print("uppercase :- ",str.upper())
# print("lowercase :- ",str.lower())
# print("length of string :- ",len(str))
# print("replace char :- ",str.replace("boy","girl"))


# write a python program to check whether a given word is a palindrome or not using string slicing

# word=input("enter a word :- ")

# reverse = word[::-1]

# if word==reverse:
#     print("word is palindrome")
# else:
#     print("word is not palindrome")




# create a list of 10 numbers and perform the following operations:
# Add a new element
# Remove an element
# sort the list
# find the maximum and minimum value

# lst=[1,8,4,9,7,2,2,1,0,2]

# print("list :- ",lst)

# lst.append(75)
# print("new list :- ",lst)

# lst.remove(8)
# print("remove an element :- ",lst)

# lst.sort()
# print("sort the list :- ",lst)

# print("maximam value :-",max(lst))
# print("minimum value :- ",min(lst))



# write a python program to count how many even 
# and odd numbers are present in a list

# lst=[2,7,6,5,9,4,7,9,4]

# print("list :- ",lst)

# even=0
# odd=0

# for i in lst:
#     if i % 2 == 0:
#         even+=1
#     else:
#         odd+=1

# print("Total even number in list :- ",even)
# print("Total odd number in list :- ",odd)


# create a tuple contaning 5 subjects print :
# first element, last element, length of the tuple,
#  check whether a subject exists in the tuple or not

# tpl=("math","cpp","python","java","DSA")

# print("my tuple :- ",tpl)

# print("first element :- ",tpl[0])
# print("last element :- ",tpl[4])
# print("length of tuple :- ",len(tpl))

# sub=input("enter a subject :- ")
# if sub in tpl:
#     print("subject exist in tuple")
# else:
#     print("subject not exist in tuple")




#  write a python program to create a dictionary of student details contaning
# Name, Age, Course, Marks

# student={
# "name":input("enter your Name :- "),
# "Age":int(input("enter your age :- ")),
# "course":input("enter your Course :- "),
# "marks":int(input("enter your Marks :- "))
# }

# print("student details :- ",student)





# write a python program to update and delete element from a dictionary

# marks={
#     "math":75,
#     "phy":67,
#     "python":86,
#     "java":87,
#     "DSA":75
# }

# print("marks :- ",marks)

# marks["math"]=90
# print("update marks :- ",marks)

# del marks["java"]
# print("After delete :-",marks)


# Create two sets and perform the following set operation
# union, intersection, difference, symmetric difference

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# print("union of set :- ",set1.union(set2))
# print("intersection of set :- ",set1.intersection(set2))
# print("difference of set :- ",set1.difference(set2))
# print("symmetric difference :- ",set1.symmetric_difference(set2))


# write a python program to remove duplicate elements from a list using a set

# lst=[1,2,2,3,3,5,6,6,3,7,8]
# set1=set(lst)
# print("your set :- ",set1)




