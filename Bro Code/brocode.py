        #       args 

# def sum(*args) : 
#     sum =0  
#     for val in args : 
#         sum += val
#     return sum 

# print(sum(1 , 2))
# print(sum(1 , 2 , 3))
# print(sum(1 , 2 , 3 , 4 , 5 , 6 , 7 , 8))



        #      kwargs   

# def hello(fname  , lname ): 
#     print("hello " + fname +" "+ lname)
# hello(fname = "mohamed" , lname = "khalifa")
# # hello(fname = "mohamed" , mname = "khalifa" ,  lname = "abbas")  error 


# def hello(**kwargs) : # kwargs not keyword >> def hello(**names) (correct)  
#     print("hello" , end=" ") 
#     for key ,val in kwargs.items() : 
#         print(val , end=" ")

# hello(fname = "mohamed" , mname = "khalifa" ,  lname = "abbas")


    # string format 

animal = "cat"
iteam  = "moon"

# print("the "+animal+"jumbed over the "+iteam)
# print("the {} jumbed over the {}".format(animal , "moon"))
# print("the {1} jumbed over the {0}".format(animal , "moon"))

# text = "the {} jumb over the {" ":10}"
# print(text.format(animal , iteam))


# pi = 3.14139
# num = 100000230
# print("the pi is {:.2f}".format(pi))
# print("the num is {:,}".format(num))
# print("the num is {:b}".format(num)) # binary code
# print("the num is {:o}".format(num)) # octol 8
# print("the num is {:x}".format(num)) # hexa 16
# print("the num is {:E}".format(num)) # النظام العالمي


#       Random

# import random 

# num  = random.randint(1, 6)
# print(num)

# l = ["ahmed" , "mohamed" , "khalifa"]
# print(random.choice(l))

# cards = [1 , 2, 3 ,4  , 5, 6 , 7 , 8 ,9 ,'j' , 'q' , 'k' , 'a']

# random.shuffle(cards)

# print(cards)

# try : 
#     numerator = int(input("enter anumber to divide "))
#     denomerator = int(input("enter anumber to divide by "))
#     res = (numerator/denomerator)

# except ZeroDivisionError : 
#     print("you can not divide by zero")
# except ValueError :
#     print("only numbers")
# except Exception as e :
#     print(e)     
# else : 
#     print(res)
# finally : 
#     print("this always execute")



 #      File detiction 
  
# import os

path = r"F:\AI\python\folder\text.txt"

# if os.path.exists(path) : 
#     print("file is exist")
#     if os.path.isfile(path) : 
#         print("yes is a file")
#     elif os.path.isdir(path) : print("this is folder")    
# else : 
#     print("file not exist")    



# try : 
#     with open(path) as file : # deafult open(path , 'r')  reed mode
#         print(file.read())

# except FileNotFoundError  : 
#     print("file not exist")

# text = 'you are very nice \n have a good day\n'
# try : 
#     with open(path , 'w') as file : # write >> delete all content in file and write the new tex
#         # file.write(text)
#         pass
# except FileNotFoundError  : 
#     print("file not exist")

# try : 
#     with open(path , 'a') as file : # append new content with old content
#         file.write(text)

# except FileNotFoundError  : 
#     print("file not exist")


# try : 
#     with open(path) as file : # deafult open(path , 'r')  reed mode
#         print(file.read())

# except FileNotFoundError  : 
#     print("file not exist")


#         Copy files 

# copyfile()  >> Copies the contents of the source file (src) to the destination file (dst). Does not copy file metadata
# copy()      >> copyfile() file data  + file permission   
# copy2()     >> copyfile() file data  + Copies all file metadata  

# import shutil   

# shutil.copyfile(r"F:\AI\python\folder\text.txt" , r"F:\AI\python\folder\copy1.txt")   # src , destntion



#       Move file

# import os 
# src = r"F:\AI\python\folder\copy1.txt"
# des = r"F:\AI\python\copy1.txt" 

# try : 
#     if os.path.exists(des) : 
#         print("there is already file there")
#     else : 
#         os.replace(src , des) 
#         print(src + " was moved")    
# except FileNotFoundError : 
#     print("path not exist")



#      remove files 

# import os 
# import shutil
# try : 
#     os.remove(r"F:\AI\python\copy1.txt") # remove file
#     os.rmdir(r"F:\AI\python\empty_folder") # remove empty folder
#     shutil.rmtree(r"") # remove not empty folder
# except FileNotFoundError as e : 
#     print(e)    
# except PermissionError : 
#     print("you do not have a permision to do it")    

# else : 
#     print("was deleted")    



#       module 

# import meesege  as msg 

# msg.hello()
# msg.bye()

# help("modules")




#       rock , paper, scissors game

# import game 
# game.rps_game()      


#      walrus operator or assigment operation  :=


# happy =  True 
# print(happy)

# print(happy := True)


foods = []

while food := input("what food do you like ?") != 'q' : 
    foods.append(food)



#        functions to varibels 

def hello() : 
    print("hello")


# h = hello 
# h() 

# p = print 
# p("ahmed")


#              higher order functions
def loud(text) : 
    return text.upper()


def quiet(text) : 
    return text.lower()

def hello(func) :
    text = func("hello")
    print(text) 

# hello(loud)    


#    lambda  
#  function write in 1 line , accept any num of argemnts but return on expression

double   = lambda x : x *10 
multiply = lambda x , y : x * y
add      = lambda x , y , z : x + y + z


# print(double(2))
# print(multiply(2 ,4))
# print(add(1,22 ,2))


# #       filter (function , itreable)


friends = [ ("mohamed" , 18) ,
            ("ahmed" , 16) ,
            ("kareem" , 17) , 
            ("abdallh " , 19) ,
            ("hazem" , 20)
           ]

age_fun = lambda age : age[1] >= 18 

new_friends = list(filter(age_fun , friends))


# for i in new_friends : 
#     print(i)



#        reduce(function , itreable) 

import functools 

w = ['h' , 'e' , 'l' , 'l' , 'o']

word = functools.reduce(lambda x , y : x+y  , w )
# w = ['h'  , 'e' , 'l' , 'l' , 'o']
# w = ['he' , 'l' , 'l' , 'o']
# w = ['hel' , 'l' , 'o']
# w = ['hell' , 'o']
# w = ['hello']

# print(word)

factroil = [5 , 4 ,3 ,2 ,1] 
res = functools.reduce(lambda x ,y : x*y  , factroil)

# print(res)


#          zib() 

usernames = ['Mohamed khalifa' , 'mohamed khaled' , "ahmed eid"]
passwords = ['M123' , 'khaled22' , "a15@"]
date = ['19/7/2024' , '2/5/2024' , "1/1/2022"]

users = zip(usernames , passwords , date)


# for i in users :
#     print(i)




