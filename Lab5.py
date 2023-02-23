'''
Lab 5: If Statement in Python
'''

#3.1
alien_color= 'green'
if alien_color == 'green':
        print('you got 5 points')

#3.2
if alien_color == 'green':
   print('you got 5 points') 
else:
    print('you got 10 points')
    
#3.3 
favorite_fruits = ['apple', 'bananas', 'watermelon']
if 'apple' in favorite_fruits:
    print('I really like apples')
if 'grapes' in favorite_fruits:
    print('I really like grapes')
if 'bananas' in favorite_fruits:
    print('I really like bananas')
    
#3.4
age = 21
if age<10:
    print('person is a kid')
elif age<20:
    print('person is a teenager')
elif age>=65:
    print('person is an elder')
else:
    print('this person is an adult')

