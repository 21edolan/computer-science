#035
user_name = input('enter your name:')
for character in range(3):
    print(user_name)

#036
user_name = input('enter your name:')
num1 = input('enter a number:')
num1=int(num1)
for character in range(num1):
    print(user_name)

#037
my_string=input('enter your name:')
for character in my_string:
    print(character)
    
#038
my_string=input('enter your name:')
num1=input('enter a number:')
num1=int(num1)
for character in my_string:
    print(character*num1)
    
#039
num1=input('enter a number between 1 and 12:')
num1=int(num1)
for number in range(num1,num1*12,num1):
    print(number)
    
#040
num1=input('enter a number below 50:')
num1=int(num1)
for character in range(50,num1-1,-1):
    print(character)

#041
user_name = input('what is your name?:')
num1=input('enter a number:')
num1=int(num1)
if num1<10:
    for character in range(num1):
        print(user_name)
else:
    for character in range(3):
        print('too high')
        
#042
total=0
for character in range(5):  
    num1=input('enter 1 numbers:')
    num1=int(num1)
    m = input('do you want to add that number?:')
    m=m.lower()
    if m=='yes':
        total=total+num1
print(total)

#043
direction=input('do you want to count up or down?:')
direction=direction.lower()
if direction=='up':
    num1=input('enter the top number:')
    num1=int(num1)
    for character in range(1,num1+1,+1):
        print(character)
if direction=='down':
    num1=input('enter a number below 20:')
    num1=int(num1)
    for character in range(20,num1-1,-1):
        print(character)
else:
    print('i dont understand!')
    
#044
for character in range(9):
    num1=input('how many people do you want to invite to a party?:')
    num1=int(num1)
    if num1<10:
        name=input('enter a name:')
        m = input('do you want to add that number?:')
        m=m.lower()
        if m=='yes':
            total=
            print(total)