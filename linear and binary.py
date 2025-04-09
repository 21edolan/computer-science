#1
key=input('enter the key:')
key=int(key)
l=[-4,-2,0,3,4,6,10,14,15,18,20,24,26,27,29,30,31,44,47,49]
idx=0
match=False
for x in l:
    if x==key:
        match=True
        print(l.index(x))
    
if not match:
    print('-1')
#2
L=[-4,-2,0,3,4,6,10,14,15,18,20,24,26,27,29,30,31,44,47,49]
targetval=input('enter the target value:')
targetval=int(targetval)
low=0
high=len(L)-1
mid=low+high//2
while low<=high:
    mid=int((low+high)//2)
    if L[mid]==targetval:
        print('amount of elements checked is:',mid)
        break
    elif L[mid]<targetval:
        low=mid+1
    elif L[mid]>targetval:
        high=mid-1


