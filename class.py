# string data types in python

# name="upflairs"
# print("this is my string :- ",name)
# # print("type of my stgring :- ",type(name))  # type fuction used for find data type
# num="123456"
# print("type of my stgring :- ",type(num))    

# name="upflairs"
# print("len of my first string",len(name))

# indexing and slicing
# print(name[2])       #indexing start from 0
# print("slicing :- ",(name[0:2]))   #sclicing start from 1

# print(name[-1])
# print(name[-1:-3])    # find reverse                  (task 1)

# lower case to upper case

# company_name="upflairs pvt ldt"
# upper_case=company_name.upper()
# print("epper case :- ",upper_case)

# upper case to lower
# lower_case=company_name.lower()
# print("lower case :- ",lower_case)

# lower_case=company_name.casefold()                     # task 2
# print(lower_case)


# company_name="upflairs pvt ltd"
# irst_latter=company_name.title()  # title each letter ke first word ko capital karta hai
# print(first_latter)

# second_latter=company_name.capitalize()    # only first letter ke first word capital
# print(second_latter)

# name="rehan"
# c=name.count('r')
# print(c)

# print(name.index('e'))  # find index of a character

# name="rehan"
# last_name="alam"
# print(name+last_name)
# print(name,last_name)
# print("😊",name,last_name)

# name="rehan " #number can multiply by str (str can not mul,div,sub by str)
# print(name*5)


# multiple line string by triple inverted coma(""")
# paragraph="""A paragraph is a group of sentences that talk about one main idea or topic. It usually starts with an indentation or a new line and helps organize writing to make it easier to read.
# Example paragraph:
# “My school is a wonderful place to learn. The teachers are kind and helpful, and I enjoy studying with my friends. We also take part in sports and cultural activities. I feel happy and motivated when I go to school.”
# A paragraph generally has:
# Topic sentence – introduces the main idea
# Supporting sentences – give details or examples
# Closing sentence – ends the idea clearly"""
# print(paragraph)

# name="rehan"
# address="bihar"
# print(f"my name is {name} and i am from {address}")  #f function use to add string

# path=r"C:\Autodesk\WI\287921268008307166" #row string use for path 
# print(path)




# >>>>>>>>>>>list data type<<<<<<<<<<<<<<<<<
# hetrogenus  (multiple types data str,int,float)
# allow dublicate value, changable
# lst=[1,2,3,"hello",3,4.2]
# print("my list:- ",lst)
# print(len(lst))

# lst=[1,2,3,"hello",3,4.2]
# print(lst[0])
# # print(lst[2])
# # print(lst[3])

# print(lst[0:3])  #slicing
# print(lst[1:2])  
# print(lst[2:4])  


# lst=[1,2,3,"hello",3,4.2,"hii"]  # add string through append
# lst.append("upflairs")
# lst.insert(0, "upflairs")  # insert perticular index
# print(lst)

# lst.remove(3)
# print(lst)



# lst.pop(3)
# print(lst)


# lst.count
# lst.clear
# lst.copy



# lst1=[1,2,3,4,5]
# lst2=[4,5,6,7,8,]
# print(lst1+lst2)
# print(lst1-lst2)
# print(lst1*lst2)
# print(lst1/lst2)
# print(lst1//lst2)
# max() 
# min()
# sum()  


# lst=[1,4,7,5,2,2,"rehan"]
# lst.reverse()
# print(lst)

# lst=[1,4,7,5,2,2]
# lst.sort()
# print(lst)


# >>>>>>>>>>>>>>>>>>>>>>>>              tuple     <<<<<<<<<<<<<<<<<<<<<<<

# tuple defination= 
# A tuple is a data structure used in programming to store multiple values in a single variable.
#  Unlike a list, a tuple is ordered and immutable,
#  which means its elements cannot be changed after creation.
# In Python, tuples are written using parentheses ().

# Example:
# my_tuple = (10, 20, 30)
# print(my_tuple)
# Key features of a tuple:
# Ordered → items keep their position.
# Immutable → you cannot modify, add, or remove items after creation.
# Allows duplicates → same values can appear more than once.
# eg = colors = ("red", "blue", "green")

# tpl=(1,13,14,15,15,"hii","rahul")
# print("this is my tupple",tpl)
# print(type(tpl))
# print(len(tpl))

# index and slicing
# print(tpl[0])
# print(tpl[3])
# print(tpl[2:5])

# print(tpl)
# print(tpl.count(15))
# print(tpl.index(14))


# a=1,2,3,"hello","hii"
# print(a)
# print(type(a))
# print(len(a))


# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)

# a,b=(1,2,3)
# print(a)   #error
# print(b)




# <<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>><<<<<
#  type casting  =    tupple ko list me convert karna 
#                     fir item revove or add karna fir list ko tupple banana


# tpl=(1,2,3,4,5,"hii","rahul")
# print("<<<<<<<tupple convert into list>>>>>>>")
# lst=list(tpl)
# print("this is my list :- ",lst)
# print(type(lst))
# print("add item in list--------------")
# lst.append("adding iten....")
# print("item add ho chuke------------",lst)
# print("list convert into tupple------------")
# tpl=tuple(lst)
# print("my tupple :- ",tpl)
# print(type(tpl))
# print("tupple me item add ho chuke-----------")

# <<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>






#>>>>>>>>>>>>>     dict     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#dictionary it is key of dict 
#dict don't allow dublicate key 
#dict allow dublicate value 
#item = pair of ( keys+ values )

# student={"name":"rehan",
#          "class":"3rd year",
#          "subject":"python",
#          "roll_no":42,
#          "branch":"cse"}

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# print(student['name'])
# print(student['class'])
# print(student['subject'])
# print(student['branch'])
# print(student['roll_no'])

# print(student.get('name'))
# print(student.get('class'))
# print(student.get('branch'))
# print(student.get('subject'))
    
#                            ques       copy and deep copu

#<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# car={"brand":"honda",
#      "mode":2026,
#      "owner":"first owner",
#     "car name":["honda city","honda amaze","honda elevate"]}  # multiple value
# print(car)
# print(car['car name'])


# car['car name']="BMW"                #add item  
# car['mode']=2026
# print(car)



# x =car.setdefault('colour','white')        #default value
# print(x)
# print(car)


# for x in car.keys():           # find key usng loop
#     print(x)

# for x in car.values():               # find value usng loop
#     print(x)

# for x in car.items():               # find item using item
#     print(x)





# <<<<<<<<<<<<<<<>>>>>>>>>>>                  SET           <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>

#  Definition:  mutable (can add item)
#“A set is a data type used to store multiple items in a single variable, 
# where duplicate values are not allowed.”

# sat = {1,2,3,4}
# print(sat)
# print(len(sat))
# print(type(sat))

# sat.add(10)
# print(sat)

# sat.remove(1)   # if value not exist give output error
# print(sat)


# sat.discard(10)  # if value not exist output not effect(no error)
# print(sat)


#<<<<<<<<<<   python set operator      >>>>>>>>>>>>>>>>>>>>>>>>>


# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1|s2)                                      #union 
# result=s1.union(s2)
# print(result)

# result=s1.intersection(s2)                        #find same values
# print(result)

# a={1,2}
# b={1,2,3,4}

# print(a.issubset(b))
# print(b.issuperset(a))

#“A subset is a set whose all elements are contained in another set.”
#In simple words, if every element of one set is found in another set, 
# then it is called a subset.


#“A superset is a set that contains all the elements of another set.”
#In simple words, if one set includes every element of another set, 
# then it is called a superset.

#<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>

