import this #the zen of phython:pythonic
#white spacing formatting 
#whitespace is ignored inside parenthesis and brackets
print(  1+15+
            4564)
1 + 2 + \
12+456 #can use a backslash to move to a new line
#is operator 
#all values and date containers in python are objects 
#id () function returns the "identity" of an object
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(id([1,2,3]))
#is operator compares the identit of two objects
#== operator comparess the values of two objects 

print(a == b)

print(a is b)

print(id(a))
print(id(b))
print(id(1))

print(a == b)
print( a is b)

#none type
#none is datatype of its own that indicates no value
#check if a variable is none: "x is none" or "x==none"
#only none values are none

a= None

print(id(a))
print(id(None))

print(a is None)
print(a == None)

x=[]
print(x is None)

x= ""
print(x is None)

x= ()
print(x is None)

x= None
print(x is None)

#boolean type 
#2 types: True or False 
#use and, or, not operators 
#x or y: if x is False, then y, else x
#x and y: if x is False, then x, else y
#not x: if x is false, then true, else false

print(True and False)
print( not True)
print(not 0)

print(not None)
print(not '0')

print(1<2)

if 2<1 :
    print("2>1") #nothing will be printed because the beginning is false
    
if 2>1:
    print("2>1")
    print('another 2>1')
    
print('out of if block')

if 2>1:
    print("2>1")
    print('another 2>1')
    if 3>1:
        print('3>1')
    else:
        print('else statement')
        
print('out of if block')

if 2>1:
    print('2>1')
elif 3>1:
    print('3>1')