#5
string=input('enter a string:')
length=len(string)
a=0
end=length
string2=''
while a<length:
    if a==0:
        string2+=string[0].upper()
        a+=1
    elif (string[a]==''and string[a+1]!=''):
        string2+=string[a]
        string2+=string[a+1].upper
        a+=2
    else:
        string2+=string[a]
        a+=1
print('original string:',string)
print('Capitilised words string:',string2)
#6
string=input('enter a string:')
length=len(string)
mid=int(length/2)
rev=-1
for a in range(mid):
    if string[a]==string[rev]:
        a+=1
        rev-=1
    else:
        print(string,'is not a palindrome')
        break
else:
    print(string,'is not a palindrome')
#7
string=input('enter a string:')
length=len(string)
maxlength=0
maxsub=''
sub=''
lensub=0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lensub>maxlength:
            maxsub=sub
            maxlength=length
            sub=''
            lensub=0
    else:
        sub+string[a]
        lensub=len(sub)
    a+=1
print('Maximum length consonant substring is:',maxsub,end=' ')
print('with',maxlength,'characters')
#8
string=input('enter a string:')
length=len(string)
print('original string:',string)
string2=''
for a in range(0,length,2):
    string2+=string[a]
    if a<(length-1):
        string2+=string[a+1].upper()
print('alternatively capitalised string:',string2)
#9
email=input('enter your email id:')
domain='@edupillar.com'
ledo=len(domain)
lema=len(email)
sub=email[lema-ledo:]
if sub == domain:
    if ledo!=lema;
        print('it is valid email id')
    else:
        print('this is valid email id - contains just the domain now')
else:
    print('this email-id is either not valid or belongs to some other domain')
    