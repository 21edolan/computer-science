L=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
targetval=28
low=0
high=int(len(L)-1)
while low<=high:
    mid=int((low+high)//2)
    if L[mid]==targetval:
        print('value is at location:',mid)
        break
    elif mid<targetval:
        low=mid+1
    elif mid>targetval:
        high=mid-1
