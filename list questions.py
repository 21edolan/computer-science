#11.3.3
lst=[10,12,14,20,22,24,30,32,34]
seq=lst[3:-3]
print(seq)
seq[1]=28
print(seq)

lst=[10,12,14,20,22,24,30,32,34]
lst[3:30]
print(lst)
lst[-15:7]
print(lst)

l1=[2,3,4,5,6,7,8]
l1[2:5]
print(l1)
l1[6:10]
print(lst)
l1[10:20]
print(l1)

#11.2
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
slc1=lst[5:15:2]
slc2=lst[ : :4]
sum=avg=0
print('slice1')

for a in slc1:
    sum+=a
    print(a,end=' ')
print()
print('sum of elements of slice1:',sum)
print('slice2')
sum=0
for a in slc2:
    sum+=a
    print(a,end=' ')
print()
avg=sum/len(slc2)
print('average of elements of slice2:',avg)

l=['one','two','THREE']
l[0:2]=[0,1]
print(l)
l=['one','two','THREE']
l[0:2]='a'
print(l)

#11.4
lst1=[10,12,14,16]
lst1.append(16)
print(lst1)

lst1=[10,12,14,16]
lst1[2]=24
print(lst1)

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10]
print(lst)

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10:15]
print(lst)

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst.pop()
print(lst)
lst.pop(10)
print(lst)

#11.5

#1-the index method=
l1=[13,18,11,16,18,14]
l1.index(18)
print(l1)

#2, the append method=
colours=['red','green','blue']
colours.append('yellow')
print(colours)

#3, the extend method=
t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)
print(t2)

#4, the insert method=
t1=['a','e','o','u']
t1.insert(2,'i')
print(t1)

#5, the pop method=
t1=['k','a','e','i','p','q','u']
ele1=t1.pop(0)
print(ele1)
ele2=t1.pop()
print(ele2)
print(t1)

#6, the remove method=
t1=['a','e','i','p','q','a','q','p']
t1.remove('a')
print(t1)
t1.remove('p')
print(t1)

