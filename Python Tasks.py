#●Create a Boolean variable named x

x=True

#●Create an integer variable named y

y=7

#●Create a float variable named z

z=5.11

#●Create a string variable names s

s="Kamal El Sayed"

#●Convert the int variable to float

a=4
float==(a)
print(a)


#●Can we convert the str to int ?

    # yes we can if the str is number but if the the str is "Kamal El Sayed"

#●Create a list of numbers from 1 to 5

x=[1,2,3,4,5]
print(x)

#●Create a tuple from 10 to 15

a=(10,11,12,13,14,15)
print(a)

#●Convert the list to tuple

x_tuple-tuple(x)

#●Create a dict of 3 values

{"name" : "Kamal El Sayed" , "age" :"22", "address" : "mansoura"}

#●Can we use semi colon ; with python

#->No

#●Python is interpreted or compiled ?

#->interpreted

#●What is the differences between 1-low level & 2-high level?

#->1-low level language : is the machine language , It is tough to understand ,It is complex.

#->2-high : very easy to human , It is simple.

#●What is the differences between = , ==

#-> the = is assignment with variable. but == is cheek the conditon is true or false or is qutation .

#●What do we mean by using!=

#->is not equal

#●What is the operator precedence?

#->1-Multipication

#->2-Division 

#->3-Addition

#->4-Subtraction

#●Create a variable x with value of 10?

x=10

#●Increase x value by 15 using assignment operators?

x+=15

#●Divide the x value by 5 using assignment operators?

x/=5

#● Multiply the x value by 10 using assignment operator?

x*=10

#●Get module of x on 3 using assignment operators?

x%=3

#●Using python print the module of 11 to 4?

print(11%4)

#●Print the exponent of 2,3 ?

print(2**3)

#●Divide 11 by 3 using python division

print(11/3)

#●Can we divide 11 by 3 and get an integer number ?

#->yes

print(11//3)

#●Check if 10 is bigger than 15 or not?

if 10>15:
    print("10 is bigger than 15")
else :
    print("15 is bigger than 10")


#●If 10 is not bigger than15 print x is smaller than 15?


if 10>15:
    print("10 is bigger than 15")
else :
    print("x is smaller than 15")

#●In which cases we will use all?

#->If we need all the conditions to be true.

#●What is the differences between all , and?
    
#-> all==>When there are more than two conditions, they must be true.
    
#-> and==>When two conditions exist, they must be true.

#●What is the differences between any , or?
    
#-> any==>When there are more than two conditions, at least one must be true.
#-> or==>When there are two conditions, at least one of them must be true.

#●If we need all the conditions to be true we will use ….

#->all

#●What is the differences between if , elif
    
#-> if ==>   It can be used once in a conditional sentence.
    
#-> elif ==> It can be used more than once in a conditional sentence.



#●What is the differences between elif, else?
    
#-> elif ==> It can be used once in a conditional sentence.
    
#-> else ==> It can be used more than once in a conditional sentence.


#●Can we use more than one elif?

#->yes

#●Can we use more than one else?

#->No


#●write s simple ternary operator?
    
print("The number is even") if (int(input("Enter the number"))%2==0) else print("The number is odd")


#●in elif , python will check all the conditions no matter what?

#->No

#●in elif we use else for ... ?

#->If all conditions are false.


#●if we have this list [2,4,6,8,10] :

    #○ check to see if 4 in this list or not
    
    #○ check to see if 4 and 6 in this list on not
    
    #○ check to see if 3 or 6 in this list
    
    #○ check to see if 2 , 4 and 5 in this list

x=[2,4,6,8,10]


if 4 in x:
    print("4 in the list")
if 4 in x and 6 in x:
    print("4 and 6 in the list")
if 3 in x or 6 in x:
    print("3 or 6 in the list")
if all([2, 4, 5]) in x:
    print("2 , 4 and 5 in the list")























