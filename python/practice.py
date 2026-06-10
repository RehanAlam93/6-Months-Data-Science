# name="hello i am mr rehan alam"

# print(name.title())
# print(name.capitalize())

# print(type(name))
# print(len(name))

# print(name[4])
# print(name[0:5])          # (start:stop)

# print(name[6:-5])      # remove last 5 index   

# print(name.split())                     # split string ko list banata hai
# print(' '.join(name.split()[::-1]))       #reverse 
# print(' '.join(name.split()[::-1][:2]))       # stop index 2


# >>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>

# name="upflairs"
# print(name[:-1])    # output = upflair

# name="private lmt upflairs"
# print(len(name))
# print(name.title())
# print(name.capitalize())
# print(name[5])
# print(name[0:10])
# a=(' '.join(name.split()[::-1][:1]))
# print(a)


# company_name="zetron network"
# s=(' '.join(company_name.split()[::-1][:2]))
# print(s)


# name="hii am rehan alam"
# a=name.count('a')
# print(a)

# name="rehan"
# last_name=" alam"
# print(name,last_name)

# name="private lmt upflairs"
# check_name=name.find('v')      # show index vlue of v
# print(check_name)

# name="private lmt upflairs"
# chr_find='z' in name    #true or false
# print(chr_find)


# name="rehan"
# address="bihar"
# college_name="cit"
# print(f"hello my name is {name} alam")
# print(f"i am from {address} india")
# print(f"my college name is {college_name} abu road")

# <>>>>>>>>>>>>>>>>>>><      copy      >>>>>>>>>>>>>>>>>>>><<<<<<<<<<<

# lst=[1,2,3,4,5,6,7,8,9,0]
# new_lst=lst.copy()
# new_lst.append(91)
# print(new_lst)
# print(lst)

# new2=lst
# new2.append(99)
# print(new2)
# print(lst)

# <<<<<<<<<<<<>>>>>>>>>>>>>>>><<<<     tuple            <<<<<<<<<<<<<<<<>>>>>>>>>>>>>><<<<<<<<<<
    # ques :- convert tupple into list then modify the list then re-convert into tupple

# tpl=(1,2,3,3,"rehan")
# print(tpl)
# lst=list(tpl)
# print(type(tpl))
# print(lst)
# print(type(lst))
# lst=lst.copy()
# lst.append("hello")
# print(lst)
# print(type(lst))
# tpl=tuple(lst)
# print(tpl)
# print(type(tpl))


# tpl=(3,3,3,4,5,6,"aadila","rahaul")
# print(tpl)
# print(type(tpl))
# print(len(tpl))
# print(tpl.count(3))
# print(tpl.index(5))

# tpl=(1,2,1,2,"hello","good")
# print(tpl)
# print(tpl[2])
# print(tpl[0:4])
# print(tpl[0:5])




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   operator in py <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<< arthmetic operator 
# x= 70
# y= 60
#<<<<<<<<<<< logical operator 
# print("multiplication of x*y : ",x*y)

# <<<<<<<<<<<<<<    comparision operator
# print("comparision x<=y : ",x<=y)
# print("x is not greater : ",not(x<y))
# print("greater and equal to : ",x>y and y==x)
# print("greater or equal : ",x>y or x==y)

# <<<<<<<<        assingment operator
# <<<<        assign value x = 70
# x+=10
# print("x + 10 : ",x)
# x-=30     # x=80 (x+10=80)
# print("x - 30 : ",x-30)

# <<<<<<<<<<<<<<    Bitwise operator
# print("bitwise AND(&) : ",x & y)

# <<<<<<<<<<       membership operator 
# my_fruit = ("apple","mango","banana","orange")
# print("is grapes in my_fruit : ","Grapes" in my_fruit)
# print("is mango in my_fruit : ","mango" in my_fruit)

#>>>>>>>>>>>>>>>>>>>>>>    identity operator 
# x=[1,3,5]
# y=x
# z=[3,4,5]
# print("x is y : ",x is y)
# print("y is z : ",y is z)
# print("x is not y : ",x is not y)



# s1={1,2,3,3,4,7}
# s2={5,4,3,2,1}
# print(s1)
# print(s2)
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.issubset(s2))


# dict          <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>

# student={
#     "name":"rehan",
#     "age":22,
#     "college":"CIT",
#     "branch":"CSE",
#     "batch":"2023-27"
# }
# print(x)
# print(x["name"])

# x['name']="shanu"
# print(x["name"])
# print(x)

# for x in student.keys():
#     print(x)
# for y in student.values():
#     print(y)
# for z in student.items():
#     print(z)



# tpl=("rehan","aman","rahul")
# print(tpl)
# lst=list(tpl)
# print(type(lst))
# lst.append('rohit')
# print(lst)
# lst.remove('rahul')
# print(lst)
# tpl=tuple(lst)
# print(type(tpl))

# print(tpl[0])
# print(tpl[0:3])


# name="i am a boy"
# print("index value 4 :",name[7])
# print("slicing value(0:8)",name[0:4])

# <<<<<<>>>>>>>>>>>>   dictionary
# student = {
#     "name": "Rehan",
#     "age": 16,
#     "class": 10
# }
# print(student)
# found = False
# for x in student:
#     if x == "branch":
#         found = True
#         break

# if found == True:
#     print("branch available")
# else:
#     print("branch not available")

# student['branch']="CSE"
# print(student)

#<<<<<<<<<<<<<<<<<<   ####################   >>>>>>>>>>>>>>>>>>>>>>>     ####################

# numbers = [12, 5, 18, 7, 20, 3]   # print greater than 10
# num=10
# for x in numbers:
#     if x > num:
#         print(x)
 

# numbers = [4, 15, 8, 22, 10, 30]   # print greater than 10 &  count
# count = 0
# num = 10
# for x in numbers:
#     if x > 10:
#         print(x)
#         count+=1
# print("number greater than 10 : ",count)
    

# text = "python"   # print python in a line
# for x in text:
#     print(x)

# text = "banana"   # count a
# count=0
# for x in text:
#     if x == "a":
#         count+=1
# print(count)

# numbers = (5, 10, 15, 20, 25)    # print divisibe by 2  numbers
# for x in numbers:
#     if x%2==0:
#         print(x)


# numbers = {2, 7, 10, 15, 18}    # print numbers > 10 
# for x in numbers:
#     if x > 10:
#         print(x)

# student = {                       # print keys
#     "name": "Rehan",
#     "age": 16,
#     "city": "Delhi"
# }
# for x in student:
#     print(x)


# marks = {          # print sub name jiska marks > 50 
#     "math": 85,
#     "english": 45,
#     "science": 72,
#     "hindi": 30
# }
# for x in marks:
#     if marks[x]>50:
#         print(x)
#         print(marks[x])


# marks = {          # print marks
#     "math": 85,
#     "english": 45,
#     "science": 72,
#     "hindi": 30
# }
# for x in marks:
#     print(marks[x])


# numbers = [12, 7, 18, 5, 21, 30]  # divisible by 2 and 3 both
# for x in numbers:
#     if x%2==0 and x%3==0:
#         print(x)


# numbers = [8, 25, 3, 40, 17] # print max number use loop
# z=numbers[0]
# for x in numbers:
#     if x>z:
#         z=x
# print(z)

# text = "python"   # reverse using loop
# rev = ""
# for x in text:
#     rev=x+rev
# print(rev)

# text="technology"
# rev=""
# for x in text:
#     rev=x+rev
# print(rev)

# numbers = [1, 2, 2, 3, 4, 4, 5]   # remove dupli... use loop
# lst=[]
# for x in numbers:
#    if x not in lst:
#       lst.append(x)
# print(lst)

# numbers = [1, 2, 2, 3, 3, 3, 4]  # store in dict how many times comes each number
# freq={}
# for x in numbers:
#     if x in freq:
#         freq[x]+=1
#     else:
#         freq[x]=1
# print(freq)


# def ask():                          # function
#     print("hello bro , kaise ho")
# ask()

# def square(num):           # function  square
#     print(num*num)
# square(10)

# def replay():                # function
#     print("badya hu bahi")
# replay()

# def add(a,b):      # function add
#     print(a+b)
# add(34,6)

# def passing():    # function
#     pass
# passing()

# lst=[1,2,3,4,5,6]       # function even odd
# def even_odd():
#     print("this is my list : ",lst)
#     for x in lst:
#         if x%2==0:
#             print("even ",x)
#         else:
#             print("odd ",x)
# even_odd()


# num="1 2 3 4".split()   # split use on string only
# print(num)

# def even_odd():       # function  input take from user

#     num=input("enter number using (,) between 2 number : ").split(",")
#     for x in num:
#         x=int(x)
#         if x%2==0:
#             print("even : ",x)
#         else:
#             print("odd : ",x)
# even_odd()



# def square():
#     number=input("enter number use space between two number : ").split()
#     for num in number:
#         num=int(num)
#         print(num," sqare : ",num*num)
# square()


# def factorial():       # factorial input by user
#     number=input("enter number use space between two num : ").split()

#     for num in number:
#         num=int(num)
#         result=1

#         for i in range(1,num+1):
#             result=result*i
#         print(num," square is  : ",result)

# factorial()


# number=int(input("enter number : "))      # factorial
# result=1
# for i in range(1,number+1):
#     result=result*i
# print("factorial is : ",result)

# class college:                       # class 
#     AC="yes"
#     smart_board="yes"
#     projector="yes"
#     student="yes"
#     teacher="yes"
#     swimming_pool="no"
#     garden="yes"
#     playground="yes"
#     liabrary="yes"
#     canteen="yes"
# cr=college
# print("is Ac : ",cr.AC)
# print("is teacher : ",cr.teacher)
# print("is  swimming_pool : ",cr.swimming_pool)



# class company:          # function in class
#     employ="yes"
#     work="yes"
#     salary="yes"
#     ac="yes"
#     def show(self):
#         print("company clean")
#         print("parking avaliale")
#         print("is AC : ",self.ac)

# cr=company()
# cr.show()



# text="hello i am rehan"
# print(text[6])
# print(text[0:6])
# print(text[-1:-6:-1])


# name="rehan alam"
# age="22"
# college="chartered institute of technology"
# print(f"my name is {name}.")
# print(f"i am {age} year old.")
# print(f"my college name is {college}")

# fruit=["apple","grapes","mango","coconut","mango"]
# print(fruit)

# fruit.remove("mango")
# print(fruit)

# fruit.append("orange")
# print(fruit)

# print(fruit.count("mango"))



