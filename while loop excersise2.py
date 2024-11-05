#1
user_number=input('enter an integer number:')
running_total=0
count=1
while user_number!='':
        user_number=int(user_number)
        running_total=running_total+user_number
        user_number=input('enter an integer number:')
        count=count+1
else:
        print('the average is:',running_total/count)
        
#2
user_number=int(input('enter an integer number:'))
running_total=0
count=1
while user_number>=0:
        user_number=int(user_number)
        running_total=running_total+user_number
        user_number=int(input('enter an integer number:'))
        count=count+1
else:
        print('the average is:',running_total/count)

#3
user_number=int(input('enter an integer number:'))
running_total=0
count=1
while user_number>=0:
        user_number=int(user_number)
        running_total=running_total+user_number
        user_number=int(input('enter an integer number:'))
        count=count+1
average=(running_total/count)
if average>=90:
    print('you achieved an A')
elif average>=80 and average<=89:
    print('you achieved a B')
elif average>=70 and average<=79:
    print('you achieved a C')
elif average>=60 and average<=69:
    print('you achieved a D')
else:
    print('you achieved an F')
    
#4
num1=int(input('enter an integer:'))
for character in range(num1,0,-1):
     print(character)
     
#5
end_value=int(input('enter an integer:'))
start_value=int(0)
while start_value<=end_value:
    if start_value %2==0:
        print(start_value)
    start_value=start_value+1
print()
