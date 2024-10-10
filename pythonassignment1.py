#program 1
user_name = input('what is your first name?')
print('hello,', user_name)

#program 2
user_name2 = input('what is your surname?')
print('hello,', user_name, user_name2)

#program 3
input('what do you call a bear with no teeth?'), print('a gummy bear!')

#program 4
num1 = input('add a number : ')
num1 = int(num1)
num2 = input('add a second number : ')
num2 = int(num2)
num3 = int(num1+num2)
print('the total is:', num3)

#program 5
num4 = input('add a number : ')
num4 = int(num4)
num5 = input('add a second number to add to that first number : ')
num5 = int(num5)
num6 = input('add a third numer to multiply by the answer of the previous two : ')
num6 = int(num6)
num7 = int(num4+num5)
num8 = int(num7*num6)
print('the answer is :',num8)

#program 6
num1= input('how many slices of pizza did you start off with? : ')
num1 = int(num1)
num2 = input('how many did you eat? : ')
num2 = int(num2)
print('the number of remaining slices is :',num1-num2)

#program 7
user_name = input('what is your name? :')
num1 = input('what age are you? :')
num1 = int(num1)
print(user_name,'next birthday you will be:', num1+1)

#program 8
num1 = input('you finished eating at a restaraunt, what is the price of your bill?: ')
num1 = int(num1)
num2 = input('how many diners are there?:')
num2 = int(num2)
print('each person must pay:', num1/num2)

#program 9
num1 = input('give me a random number of days!:')
num1 = int(num1)
num2 = int(num1*24)
print('that is equal to:',num2,'hours')
num3 = int(num2*60)
print(num3,'minutes')
num4 = int(num3*60)
print('and',num4,'seconds!')

#program 10
num1 = input('enter a weight in kg!:')
num1 = int(num1)
num2 = int(num1*2.2)
print('that is equal to',num2,'pounds!')

#program 11
num1 = input('enter a number above 100!:')
num1 = int(num1)
num2 = input('enter a number unnder 10: ')
num2 = int(num2)
num3 = int(num1/num2)
print(num2,'goes into',num1,num3,'times!')
