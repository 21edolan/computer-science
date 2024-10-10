#program 12
num1 = input('give me a number:')
num1 = int(num1)
num2 = input('give me another number:')
num2 = int(num2)
if num1>num2 :
    print(num1,'is greater than',num2)
else :
    print(num1,'is not greater than',num2)
    
#program 13
num1 = input('give me a number that is under 20:')
num1= int(num1)
if num1>20:
    print('too high!')
else:
    print('thank you<3')

#program 14
num1 = input('enter a number between 10 and 20:')
num1 = int(num1)
if num1>=10 and num1<=20:
    print('thank you!')
else:
    print('wrong answer')
    
#program 15
num1 = input('what is your favourite colour?:')
if num1=='red' or num1=='RED' or num1=='Red':
    print('i like red too!')
else:
    print('i dont like',num1,'i prefer red')
    
#program 16
num1 = input('is it raining?:')
if num1=='yes' or num1=='YES' or num1=='Yes':
    num2 = input('is it windy?:')
    if num2=='yes' or num2=='YES' or num2=='Yes':
        print('it is too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')

#program 17
num1 = input('what age are you?')
num1 = int(num1)
if num1>=18:
    print('you can vote!')
if num1==17:
    print('you can learn to drive!')
if num1==16:
    print('you can buy a lottery ticket!')
if num1<16:
    print('you can go trick-or-treating!')

#program 18
num1 = input('enter a number:')
num1 = int(num1)
if num1<10:
    print('too low!')
if num1>10 and num1<20:
    print('correct!')
if num1>20:
    print('too high!')
    
#program 19
num1 = input('enter 1, 2 or 3!:')
num1 = int(num1)
if num1==1:
    print('thank you!')
if num1==2:
    print('well done')
if num1==3:
    print('correct')
if num1!=1 and num1!=2 and num1!=3:
    print('error message')