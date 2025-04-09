key=input('enter the key:')
key=int(key)
l=[0,1,2,3,4]
idx=0
match=False
for x in l:
    if x==key:
        match=True
        print(l.index(x))
    
if not match:
    print('-1')