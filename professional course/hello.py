# # if 5 > 2:
# #     print("Five is greater than two!")
# # if 5 > 2:
# #         print("Five is greater than two!")

# # if 3 > 2:
# #     print("highest is 3")

# # variables
# # x = y = z = "orange"
# # print(y)
# # print(x)   run 
# # print(z)


# # x, y, z = "orange" , "banana", "cherry"
# # print(y)
# # print(x)    not run error
# # print(z)

# # fruits = ["apple", "banana", "cherry"]
# # x, y, z = fruits
# # print(y)
# # print(x)    not run error
# # print(z)

# # username = input("Enter username:")
# # print("Username is: " + username)
# # age = int(input("Enter your age: "))

# # if age < 18:
# #     print("cannot vote")
# # elif age <= 100:
# #     print("can vote")
# # else:
# #     print("invalid")

# # DAY2

# # s ="TEXAS"
# # for i in s :
# #     print(i)

# # for i in range (0,10,2):
# #     print(i)

# # x = [1,2]
# # y = [4,5]
# # for i in x:
# #     for j in y:
# #         print(i,j)


# # # Initial list
# # my_list = [10, 20, 30, 40, 50]
# # print(my_list)

# # # append() - Adds an element at the end of the list
# # my_list.append(60)
# # print("After append(60):", my_list)

# # # clear() - Removes all the elements from the list
# # my_list.clear()
# # print("After clear():", my_list)

# # Reinitialize list for further operations
# my_list = [10, 20, 30, 40, 50]
# print(my_list)
# # copy() - Returns a copy of the list
# my_list_copy = my_list.copy()
# print("Copy of my_list:", my_list_copy)

# # count() - Returns the number of elements with the specified value
# count_30 = my_list.count(30)
# print("Count of 30:", count_30)


# #for length (total in list)
# len = len(my_list)
# print(len)

# # extend() - Add the elements of a list (or any iterable), to the end of the current list
# my_list.extend([60, 70, 80])
# print("After extend([60, 70, 80]):", my_list)


# # # index() - Returns the index of the first element with the specified value
# # index_40 = my_list.index(40)
# # print("Index of 40:", index_40)

# # # insert() - Adds an element at the specified position
# # my_list.insert(2, 25)
# # print("After insert(2, 25):", my_list)

# # # pop() - Removes the element at the specified position
# # popped_element = my_list.pop(3)
# # print("After pop(3):", my_list)
# # print("Popped element:", popped_element)

# # # remove() - Removes the item with the specified value
# # my_list.remove(25)
# # print("After remove(25):", my_list)

# # # reverse() - Reverses the order of the list
# # my_list.reverse()
# # print("After reverse():", my_list)

# # # sort() - Sorts the list
# # my_list.sort()
# # print("After sort():", my_list)

# my_list = [ ]
# inp = int(input("enter the size of list" ))
# for i in range(inp):
#     el= input("enter the element")
#     my_list.append(el)
# print(my_list)

# mytuple = (1,2,3,4,5)
# print(mytuple)
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])

# newtuple = mytuple[1:3]
# print(newtuple)

# mytuple1 = (3,4,6,7,8)
# concatenate = mytuple + mytuple1 
# print(concatenate)

# repeated = (mytuple,mytuple1) * 5
# print(repeated) 

# count_2 = mytuple.count(2)
# print(count_2)

# index_3 = mytuple.index(3)
# print(index_3)


# length = len(mytuple)
# print(length)

# a = max(mytuple)
# print(a)

# a = min(mytuple)
# print(a)

# #creating dictionary
# mydict = {
#     "name":"Texas",
#      "location":"Mitrapark",
#       "country":"Nepal"
# }
# print(mydict)

# print(mydict["name"])
# print(mydict["location"])



# mydict["name"]="Dursikshya"
# print(mydict)


# mydict["email"]="exam@example.com"
# print(mydict)

# del mydict["email"]
# print(mydict)

# print("name" in mydict)
# print("country" in mydict)
# print("place" in mydict)


# country = mydict.pop("country")
# print(country)
# print(mydict)


# for key in mydict:
#     print(key , mydict[key])

# for value in mydict.values():
#     print(value)    



# for key , value in mydict.items():
#     print(key , value)    


# nested_dict = {
#     "person1" : {"name": "Alice", "age":25},
#     "person2" : {"name": "Bob", "age":30},
# }

# for person, info in nested_dict.items():
#     name = info["name"]
#     age = info["age"]
#     print(f"{person}: Name = {name}, Age = {age} ")

# #concatenate
# greeting = "hello"
# name = "texas"
# message = greeting +  "    " + name + "!"
# print(message)


# slic = greeting [1:4]
# print(slic)

# s = "hello"
# sliced = s[:-1]
# print(sliced)


# length = len(greeting)
# print(length)


# up_str = greeting.upper()
# print(up_str)
# low_str = greeting.lower()
# print(low_str)



# index = greeting.find('lo')
# print(index)


# gre = greeting.replace('hello','hi')
# print(gre)


# name = "Alice"
# age = 30
# intro = f"My name is {name} and i am {age} years old."
# print(intro)

# intro = "My name is {} and i am {} years old.".format(name,age)
# print(intro)

# intro = "My name is %s and i am %d years old."%(name,age)
# print(intro)


# multi_line ="""
# This is a string that spans 
# multiple lines.It's useful 
# for ling text.
# """
# print(multi_line)

# newline = "Hello\n World"
# tabbed = "Hello\t World"
# quoted = "She said, \"Hello!\""
# print(newline)
# print(tabbed)
# print(quoted)

# def add(a,b):
#     return  a + b 
# result = add(3,4)
# print(result)
 
# def greet():
#     print("Hello , World!")
# greet()

# def evenodd(a):
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")

# evenodd(6)
# evenodd(7)

# def greet(name,message):
#     print(f"{message},{name}!")
# greet(name="Texas",message="Good morning")


# def greet(name,message="Hello"):
#     print(f"{message},{name}!")
# greet("Texas")
# greet("intl","Good morning")

# def greet(*names):
#     for name in names:
#         print(f"Hello,{name}!")
# greet("Alice","Bob","Charlie")

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}is {value}")
# greet(name = "Alice", age= 25, city= "New York")
# greet(name ="Bob", profession="Developer")


# def factorial(n):
#     if n== 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     result= factorial(5)
# print(result)

# def fib(n):
#     if n<= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#     num = int(input)




