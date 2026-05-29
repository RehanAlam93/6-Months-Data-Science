# >>>>>>>>>>>>>>>>>>find reverse <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>

# name="hello i am rehan"
# reverse=''.join(reversed(name))
# print(reverse)


#>>>>>>lower case or casefold<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<<<<<<<<<<

# name="rehan"
# lower_case=name.lower()
# print(lower_case)

# case_fold=name.casefold()
# print(case_fold)


# special_chr="sakiß"                #casefold use for special character
# print(special_chr.lower())
# print(special_chr.casefold())



#>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>><<<<<<<<<<<

# lst1=[1,2,3,4]
# lst2=[5,6,7,8]
# print(lst1+lst2)         #all item write in a seq..

# print(max(lst1))         # 4 is max from lst 1
# print(max(lst2))          # 8 is max from lst 2
# print(min(lst1))         #1 is min from lst 1
# print(min(lst2))        #5 is min from lst 2

# sum=lst1+lst2
# print(max(sum))         # max is 8 from lst1+lst2

# print(list(zip(lst1,lst2)))         # zip use for make pair of same index

# result=[a*b for a,b in zip (lst1,lst2)]     
# print(result)

# div=[a/b for a,b in zip(lst1,lst2)]
# print(div)

# sub=[a-b for a,b in zip(lst1,lst2)]
# print(sub)

# mod=[a%b for a,b in zip(lst1,lst2)]
# print(mod)

#<<<<<<<<<<<<<>>>>>>>>>>>>>><<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>

# lst=[1,2,3,4,5,6,7,8,9,0]

# lst.sort()
# print(lst)

# lst.clear()
# print(lst)


num=int(input("enter a number : "))
if num>=0 and num%2==0:
    print("positive and even")
elif num>0 and num%2!=0:
    print("positive and odd")
elif num<0 and  num%2==0:
    print("negative and even")
else:
    print("negative and odd")