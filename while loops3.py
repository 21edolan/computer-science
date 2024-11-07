#1
n=int(input('enter a number value for n:'))
start_value=int(0)
while start_value<=n:
    if start_value %5!=0:
        print(start_value)
    start_value=start_value+1
print()

#2
n=int(input('enter a number value for n:'))
start_value=1
while start_value<=50:
   print(start_value**2)
   start_value=start_value+1
print()

#3
start_value=int(input('enter an integer start value:'))
end_value=29
while start_value<=end_value:
    if start_value %2==1 and start_value%5!=0:
        print(start_value)
    start_value=start_value+1
print()

#4
start_value=int(input('enter an integer start value:'))
end_value=int(input('enter an integer end value for the range:'))
num=int(input('enter a multiple to ignore:'))
while start_value<=end_value:
    if start_value %2==1 and start_value%num!=0:
        print(start_value)
    start_value=start_value+1
print()

#5
start_value=int(input('enter an integer start value:'))
start_value=50
end_value=20
while start_value>=end_value:
    if start_value%2==0 and start_value%3!=0:
        print(start_value)
    start_value=start_value+1
print()

#6
start_value=12
end_value=-14
while start_value>=end_value:
    if start_value%2==0:
        print(start_value)
    start_value=start_value-1
print()
