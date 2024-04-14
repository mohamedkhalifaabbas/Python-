print("hello python")
print("i am a programmer")
# print("i love python ")
# this is comment

# data type
# varibales not containing the data its only refer to its location on memory
# all data in python is Object
#  type()
print(10)
print(type(10))  # intger int

print(type(100.87))  # float
print(type(-100.87))  # float

print(type("hello python"))  # str String

print(type([1, 2, 3, 4, 5]))  # list => list

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"one": 1, "Two": 2, "three": 3}))  # dict => dicyionary

print(2 == 2)  # bool => Boolean
print(2 == 5)  # bool => Boolean
print(type(2 == 2))  # bool => Boolean

# ------Variables------
# Syntax
myvar = "myvalue"
print(myvar)
_myvar2 = 10
print(_myvar2)
# 2myvar2 = 10  error
# '-' dash
# '_' under score

name = "Mohamed khalifa"  # single word => normal
myName = "Mohamed khalifa"  # Two words   => camelCase
my_name = "Mohamed khalifa"  # Two words   => snake_case

# source code : Original code
# Translation : converting source code to machine language
# Compilation : translate code before run time
# Run-Time    : period app take to executing During execution
# Interpreted : code translated on hte fly during Execution
# ...........................................
# python => dynamic language

x = 10
x = "hello"
print(x)  # change data through run time

# Reserved Words
help("keywords")

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Escape Sequances

# \b   Back space
print("helloW\borld")  # will remove char w

# \newline => escape new line + \
print("hello \
world \
hi")

# Escape Back slash
print("I Love Back slash \\")

# Escape Single Quote
print("I Love single quote  \'test\' ")

# Escape Double Quote
print("I Love single quote  \"test\" ")

# Line Feed \n
print("hello world\n Second Line")

# Carriage return \r
print("123456\rABCD")  # ABCD56
print("123456\rABCDE")  # ABCDE6

# Horizontal Tab \t
print("hello\tpython")

# Charactar Hex value \xhh
print("\x4f")  # O


# ------- Concatenation -------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)
full = msg + " " + lang
print(full)

a = "Frist \
Second \
Third"

b = "A \
B \
C"

print(a + " "+b)
print(a + "\n"+b)

# print("hello "+ 2) error

# ---- Strings ----

myString1 = 'this is single quote'
myString2 = "this is double quote"
myString3 = 'this is single quote "test" '
myString4 = "this is double quote 'test' "

print(myString1)
print(myString2)
print(myString3)
print(myString4)

myString5 = "First \
Second \
Third"
print(myString5)

myString6 = """Frist
Second
Third"""

myString7 = '''Frist
Second
Third'''

print(myString6)
print(myString7)

# String Indexing & Slicing

# indexing  (Access Single item )
myString = "I love Python"
print(myString[0])  # index 0 => I
print(myString[7])  # index 7 => P

print(myString[-1])  # index -1 => frist char from end
print(myString[-6])  # index -1 => 6th char from end


# Slicing  ( Access Multiple Sequence Items )
# [Start : end]  End not encluded
# [Start : end : steps]

print(myString[7: 11])  # pyth
print(myString[2: 6])  # love

print(myString[: 6])  # start from 0
print(myString[2:])  # go to the end
print(myString[:])   # full String

print(myString[0::1])  # full
print(myString[::1])   # full
print(myString[0::2])  # Ilv yhn
print(myString[0::3])  # Io tn
print(myString[0::15])  # I


# ---- String Methods ----

a = "I love python"
print(len(a))

# strip() remove space from raight and left
# rstrip() remove space from raight
# lstrip() remove space from  left

a = "    I love Python   "
print(a.strip())
print(a.rstrip())
print(a.lstrip())


a = "######I love Python#####"
print(a.strip('#'))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "#@@#@##@I love Python@#@##@@#"
print(a.strip('@#'))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

a = "I love 2d Grsphics and 3g Techology and python"
print(a.title())

# title()

a = "I love 2d Grsphics and 3g Techology and python"
print(a.capitalize())

# zfill

c, d, e = "1", "11", "111"

print(c)
print(d)
print(e)

print(c.zfill(3))  # 001
print(d.zfill(3))  # 011
print(e.zfill(3))  # 111

# upper()
m = "mohamed"
print(m.upper())

# lower()
m = "MOhamed"
print(m.lower())

# split()   rsplit()

a = "I Love Python and Java"
print(a.split())

a = "I-Love-Python-and-Java"
print(a.split("-"))

a = "I-Love-Python-and-Java"
print(a.split("-", 2))

a = "I-Love-Python-and-Java"
print(a.rsplit("-", 2))

# center()

a = "khalifa"
print(a.center(11))
print(a.center(11, "#"))
print(a.center(11, "@"))


# count()

a = "I love python and java because python and java is very easy 'java'"
print(a.count("java"))  # 3
print(a.count("java", 0, 50))  # 2

# swapcase()

a = "I Love Python"
print(a.swapcase())  # i lOVE pYTHON


# startswith

a = "I Love Python"
print(a.startswith("I"))
print(a.startswith("M"))
print(a.startswith("P", 7, 12))

# endswith

a = "I Love Python"
print(a.endswith("n"))
print(a.endswith("N"))
print(a.endswith("e", 2, 6))


# index(substring , start , end)

a = "I Love Python"
print(a.index('P'))
print(a.index('P', 0 , 10) )
##print(a.index('P', 0 , 5)) # error


# find(substring , start , end)

a = "I Love Python"
print(a.find('P'))
print(a.find('P', 0 , 10) )
print(a.find('P', 0 , 5)) # -1


# rjust(width , fillchar)  ljust

a ="Mohamed"
print(a.rjust(10))
print(a.rjust(10 , '*'))

print(a.ljust(10))
print(a.ljust(10 , '*'))


# splitlines()

a = """Frist Line
Second Line
Third Line
"""

print(a)
print(a.splitlines())

a = "Frist Line\Second line \n third line"
print(a.splitlines())


# expandtabs()

a = "Hello\tworld\tI Love python"
print(a) 
print(a.expandtabs(2)) 


one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = ""
four  = " "
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I love python'
print(five.islower())
print(six.islower())

seven = "mohamed_khalifa"
eight = "MohamedKhalifa"
nine = "Mohamed--Khalifa"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaBbbbb"
y = "AaaaaaBbb33"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaaBbbbb"
z = "AaaaaaBbb33"
print(u.isalnum())
print(z.isalnum())


# replace(old value , new value , count)

a = "Hello One Two Three One One"
print(a.replace("One" , "1"))
print(a.replace("One" , "1" , 2))

# join(Iterable)

mylist = ["mohamed" , "khalifa" , "abbas"]
print("-".join(mylist))
print(" ".join(mylist))
print(" , ".join(mylist))
print(type(" , ".join(mylist)))



## String formating

name = "khalifa"
age = 20
rank = 10

print("My name is: " + name)
# print("My age is: " + age)  >> rror 

print("my name is %s" % "khalifa") # place holder
print("my name is %s" % name)
print("my name is %s and my age is %d and my rank is %f" %(name , age , rank) )

# %s >> string
# %d >> number
# %f >> float

# control floating point number

myNumber = 10
print("my Number is %f " % myNumber)
print("my Number is %.2f " % myNumber)

# truncate string

myLongString = "hello , i am mohamed khalifa abbas i love you all"
print("messege is %s" % myLongString)
print("messege is %.5s" % myLongString)



name = "khalifa"
age = 20
rank = 10

print("My name is: " + name)
# print("My age is: " + age)  >> rror 

print("my name is {}".format("khalifa")) # place holder
print("my name is {}".format(name))
print("my name is {} and my age is {} and my rank is {}".format(name , age , rank) )
print("my name is {:s} and my age is {:d} and my rank is {:.2f}".format(name , age , rank) )


print("messege is {}".format(myLongString))
print("messege is {:.5s}".format(myLongString))

# format money

myMoney = 50001262
print("my money in bank is {}".format(myMoney))
print("my money in bank is {:_}".format(myMoney))
print("my money in bank is {:_d}".format(myMoney))
print("my money in bank is {:,d}".format(myMoney))


# Rearrange iteam 

a , b , c = "one" , "two" , "three"

print("hello {} {} {}".format(a , b , c)) # hello one two three 
print("hello {1} {2} {0}".format(a , b , c)) # hello  two three one

x , y , z = 10 , 20 , 30 
print("hi {} {} {}".format(x , y , z))
print("hi {1} {2} {0}".format(x , y , z))
print("hi {2} {0:d} {1:.2f}".format(x , y , z))


# format in v 3.6+

my_name = "khalifa"
print("my nmae is : {my_name}")
print(f"my nmae is : {my_name}")


#.......................
### -- Numbers -- 

#  intger
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

#  float
print(type(1.5))
print(type(100.99))
print(type(.990))
print(type(-10.9))


# complex 
myComplexNum = 5+6j
print(type(myComplexNum))
print("real part is : {}".format(myComplexNum.real))
print("imag part is : {}".format(myComplexNum.imag))

# [1] you can convert from int to float or complex
# [1] you can convert from float to int or complex
# [1] you can not convert from complex to any type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
# print(int(10+9j))

# artimetic operator

print(10+30)
print(-10+30)
print(1+3.66)

print(10 - 3)
print(-30 - 13)
print(-30 - -10)

print(10 * 3)
print(10 + 9 * 100)
print((10 + 9) * 100)

print(100 / 20)
print(int(100 / 20))

print(10 % 2)
print(10 % 3)

# Exponent اس

print(2 ** 5)
print(4 ** 2)

# floar devition

print(100 // 20) 
print(110 // 20)
print(120 // 20)
print(130 // 20)





# -- list -- 

mylist = [1 , 'T' , 3.5 , "four" , True , .9]
print(mylist[0])
print(mylist[1])

print(mylist[-1]) ## last index
print(mylist[-3]) ## 3.5

print(mylist)
print(mylist[1:4])
print(mylist[1:])
print(mylist[:4])

print(type(mylist))

print(mylist[::1])
print(mylist[::2])

mylist[0 : 3] = ["a" ,  5 , "f"]


# lists Methods

# append()

myfriends = ["maher" , "abdall" , "badwi"]
myoldfriends = ["haytham" , "samah" , "ali"]
myfriends.append("mohamed")

myfriends.append(myoldfriends)

print(myfriends)
print(myfriends[3])
print(myfriends[4])
print(myfriends[4][2])

# extend()


a = [1 , 2 , 3]
b = ['a' , 'b' , 'c']

a.extend(b)
print(a)


# remove()
 ## string or y
x = [1 , 2 , 3 , "mohamed" , 4 , "mohamed" , "mohamed"]
x.remove("mohamed")
print(x)


y = [1 , 2  , 100 , 120 , -10 , 17 , 29]
y.sort()
print(y)

y.sort(reverse=True)
print(y)

# reverse()
z = [10 , 1 , 9 , "khalifa" , 200]
z.reverse()
print(z)

# clear
a = [1 , 2 , 3]
a.clear()
print(a)


# copy()

b = [1 , 2 , 3 ,4 ]
c = b.copy()

print(b) # main liast
print(c) # copied list

b.append(5)
print(b) # main liast
print(c) # copied list


# count()

d = [1 ,3  ,2 , 1  , 4 , 1]
print(d.count(1))

e = ["osiam", 'ahmed' , 'sayed' , 'ramy']
print(e.index('ahmed'))


# insert()

f = [1, 3 , 4, 5 ]
f.insert(0 , 'num')
print(f)  
f.insert(-1 , 'A')
print(f)


#  pop()

g =[1 , 2, 3 , 4 , 'A' , 'b']
print(g.pop(5))
print(g)



# Tuple 

myTuple = ("khalifa" , "mohamed")
myTuple2 = "khalifa" , "mohamed"

print(myTuple)
print(myTuple2)

print(type(myTuple2))

# tuple indexing 

myTuple = 1 , 2 , 3 , 4 ,5

print(myTuple[0])
print(myTuple[-1])

# Tuple assign values


#myTuple[2] = "three"
#print(myTuple)   'tuple' object does not support item assignment



myTuple = 'khalifa' , 'khalifa' , 1 , 2 ,3 , 10.6 , True

print(myTuple[2])





















