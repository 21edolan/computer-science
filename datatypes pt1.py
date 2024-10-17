#1
day1=input('tell me the temperature over the last seven days one at a time:')
day1=int(day1)
day2=input('temp for day 2:')
day3=input('temp for day 3:')
day4=input('temp for day 4:')
day5=input('temp for day 5:')
day6=input('temp for day 6:')
day7=input('temp for the final day:')
day2=int(day2)
day3=int(day3)
day4=int(day4)
day5=int(day5)
day6=int(day6)
day7=int(day7)
avg=int(day1+day2+day3+day4+day5+day6+day7)
print('the average temperature for the week was:',avg/7)

#2
x=input('give me a number for x:')
x=int(x)
y=input('give me a number for y:')
y=int(y)
z=input('give me an input for z:')
z=int(z)
pi=int(3.14)
answr=int(4*x**4+3*y**3+9*z+6*pi)
print('the sum following the formula 4x⁴+3y³+9z+6π is:', answr)

#3
seconds=input('give me a time in seconds:')
seconds=int(seconds)
print('that is equal to:',seconds//60,'minutes')

#4
hour=input('give me an hour between 1am and 12pm:')
hour=int(hour)
skip=input('how many hours ahead would you like to know the time?:')
skip=int(skip)
time=int(hour+skip)
print(skip,'hours later would be:',time%12,'pm')

#5
nums=input('enter a 3-digit number:')
nums=int(nums)
dig1=nums%10
dig2=nums//10
dig3=dig2%10
dig4=dig2//10
print('numbers reversed is:',dig1,dig3,dig4,sep='')


#6
day=input('enter a day of any month:')
day=int(day)
month=input('and now a month:')
month=int(month)
monthh=month*30
print('this is day',day+monthh,'of the current year')