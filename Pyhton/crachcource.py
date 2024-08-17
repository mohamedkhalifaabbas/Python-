# input

# user_input = input("enter num : ")
# print(user_input)


# # methods 

# # print(abs(-1))
# # print(max(-1 , 3))
# # print(min(-1 , 3))
# # print(len("test"))

# inp = int(input())
# inp = float(input())
# print(inp + 10)

#  power
# print(2 ** 3)
# print(pow(2 , 3))

# tuple
tuple = ("ahmed" , 123 , 'r')

list = ["ahmed" , 123 , 'r']

# a tuple can not change (immutable) while you can change the values of a list

#set = {1 , 3.9 , 'test'}
# set > every entry is unique 

# Dictionary = {name:'mohamed' , 123 : 'num' }


# a_list = [2 , 1 , 3 , 'k' , 2 , 'k' , 'h' , 4]
# print(set(a_list))


# a_dictionary = {'key': 'value' , 123:[1,2,3]}
# print(a_dictionary)
# print(a_dictionary['key'])
# print(a_dictionary[123])


print(2 == 2)
print(2 == 4)
print(5 >= 4)


# if statement
if 5 < 4:
    print("correct")
elif 2 > 1:
    print("so")
    if 2 ==3:
        print("2 !=3")
    else :
        print("else ")    
else:
    print("incrroect")   

print("test")    


# while loop
counter = 1 
while counter <= 10 :
    if counter == 2 :
        counter+=1
        continue
    else : 
     print(counter)
     counter+=1
   

# for loop

test_list = ['a', 'b', 'g' ,'k' ,5]
for x in test_list:
    print(x)


# truthy and false

if []:
    print("truthy")
else : 
    print("false")    


test_list =( 1 , 2, 3 , 4 , 5)

for i in test_list:
    if i == 2 or i == 3 :
        print('the value is %d' %(i))
    else :
        if i == 5 :
            j = 0 
            for j in 5 :
                print("last iteam")






