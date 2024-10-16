#1
radius=input('enter the radius of a circle:')
radius=int(radius)
PI=3.14
area=(PI*radius*radius)
print('the area  is equal to', area)

#2
height=input('enter your height in cm:')
height=int(height)
inches=height/2.54
feet=inches/12
print('your height in inches is:', inches,',and your height in feet is:',feet)

#3
n=input('enter the value of n:')
n=int(n)
print('n² is equal to:',n**2)
print('n³ is equal to:',n**3)
print('n⁴ is equal to:',n**4)

#4
height=input('enter the height of a triangle:')
height=int(height)
base=input('enter the base of a triangle:')
base=int(base)
print('the area of that triangle would be:', height*base/2)

#5
name=input('enter your name:')
rang=input('enter your class:')
age=input('enter your age:')
print('your name is:',name,'your class is:', rang,'and your age is:', age)
print('your name is:',name)
print('your class is:', rang)
print('your age is:', age)

#6
n=input('enter a single digit number:')
n=int(n)
if n<10:
    print((n),(n+1),(n+2),sep='')
else:
    print('try again')
    
#7
