# -*- coding: utf-8 -*-
"""python patterns & prog

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KOMczdix_0FyP984l6_JL6xB4BNzSqnL
"""

for i in range(1,5):
  print("*",end=" ")
print()

for i in range(1,5):
  for j in range(1,i+1):
    print(i,end=" ")
  print()

for i in range(1,5):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

k=1
for i in range(10,31,5):
  for j in range(1,k+1):
    print(i,end=" ")
  k=k+1
  print()

for num in range(3):
  print(' *'*3)

for num in range(3):
  print('*'*3 ,end =' ')

n=6
for num in range(n+1):
  print('*'*num)

n=6
for num in range(6,0,-1):
  print('*'*num)

n=4
spaces=3
star=1
for num in range(4):
  print(' '*spaces +'*'* star)
  spaces-=1
  star+=1

n=5
spaces=0
star=n
for num in range(n):
  print(' '*spaces+'*'* star)
  spaces+=1
  star-=1

n=4
space=3
star=1
for num in range(n):
  print(' '*space+'*'*star)
  space-=1
  star+=2

n=7
space=0
star=n
for num in range(n):
  print(' '*space+'*'*star)
  space+=1
  star-=2

n=7
space=3
star=1
for num in range(4):
  print(' '*space+'*'*star)
  space-=1
  star+=2
space=1
star=5
for num in range(3):
  print(' '*space+'*'*star)
  space+=1
  star-=2

n=5
space=2
star=1
for num in range(3):
  print(' '*space+'1'*star)
  space-=1
  star+=2
space=1
star=3
for num in range(2):
  print(' '*space+'1'*star)
  space+=1
  star-=2

num=1
n=5
space=2
star=1
for num in range(1,n//2+1):
  print(' '*space+str(num)*star)
  num+=1
  space-=1
  star+=2
space=1
star=n-2
for num in range(n//2):
  print(' '*space+str(num)*star)
  num+=1
  space+=1
  star-=2

var=5
for num in range(5):
  for col in range(5):
    print('*',end=' ')
  print()

var=5
for  row in range(1,6):
  for column in range(row):
    print('*',end=' ')
  print()

var=4
column=4
for row in range(5,0,-1):
  for col in range(row):
    print('*',end=' ')
  print()
  column -=1

var=4
space=3
star=1
for row in range(1,5):
  for sp in range(space):
    print(' ',end=' ')
  for st in range(star):
    print('*',end=' ')
  space-=1
  star+=1
  print()

var=5
space=0
star=var
for row in range(1,5):
  for sp in range(space):
    print(' ',end=' ')
  for st in range(star):
    print('*',end=' ')
  space+=1
  star-=1
  print()

var=4
space=3
star=1
for row in range(1,5):
  for sp in range(space):
    print(' ',end=' ')
  for st in range(star):
    print('*',end=' ')
  space-=1
  star+=2
  print()

var=4
space=0
star=7
for row in range(1,5):
  for sp in range(space):
    print(' ',end=' ')
  for st in range(star):
    print('*',end=' ')
  space+=1
  star-=2
  print()

var=5
for i in range(1,6):
  for j in range(i):
    print('1',end=' ')
  print()

var=5
for i in range(5):
  for j in range(5):
    print('1',end=' ')
  print()

var=5
for i in range(1,6):
  for j in range(i):
    print(i,end=' ')
  print()

var=5
num=var
for i in range(1,6):
  for j in range(i):
    print(num,end=' ')
  print()
  num-=1

var=4
space=3
star=1
num=1
for i in range(1,5):
  for spac in range(space):
    print('  ',end=' ')
  for st in range(star):
    print(num,end=' ')
  num+=1
  space-=1
  star+=1
  print()

var=4
space=0
star=4
num=4
for i in range(1,5):
  for spac in range(space):
    print('  ',end=' ')
  for st in range(star):
    print(num,end=' ')
  num-=1
  space+=1
  star-=1
  print()

var=4
for i in range(1,5):
  for j in range(i):
    print(i,end=' ')
  print()

var=5
for ev in range(2,7,1):
  for val in range(1,ev):
    print(val,end=' ')
  print()

for ev in range(6,1,-1):
  for val in range(1,ev):
    print(val,end=' ')
  print()

for ev in range(4,-1,-1):
  for val in range(5,ev,-1):
    print(val,end=' ')
  print()

for ev in range(0,5):
  for val in range(5,ev,-1):
    print(val,end=' ')
  print()

for st in range(5,0,-1):
  for val in range(st,6,1):
    print(val,end=' ')
  print()

for st in range(1,6,1):
  for val in range(st,6,1):
    print(val,end=' ')
  print()

space=4
for ev in range(2,7):
  for sp in range(space):
    print(' ',end=' ')
  for val in range(1,ev):
    print(val,end=' ')
  print()
  space-=1

space=0
for ev in range(6,1,-1):
  for sp in range(space):
    print(' ',end=' ')
  for val in range(1,ev):
    print(val,end=' ')
  print()
  space+=1

space=4
for st  in range(1,6):
  for sp in range(space):
    print(' ',end=' ')
  for val in range(st,0,-1):
    print(val,end=' ')
  print()
  space-=1

space=4
for ev  in range(4,-1,-1):
  for sp in range(space):
    print(' ',end=' ')
  for val in range(5,ev,-1):
    print(val,end=' ')
  print()
  space-=1

for num in range(0,11):
  if(num%2==0):
    print(f'{num} is even')
  else:
    print(f'{num} is odd')

# even or odd
for num in range(0,11):
  if(num%2==0):
    print('{} is even'.format(num))
  else:
    print('{} is odd'.format(num))

#factors
n=int(input())
for num in range(1,n+1):
  if(n%num==0):
    print(num)

#prime numbers
num=7
count=0
if num>1:
  for fa in range(1,num+1):
    if(num%fa==0):
      count+=1
  if (count==2):
    print('prime')
  else:
    print('not prime')
else:
  print('not prime')

#composite
n=int(input())
count=0
if n>1:
  for num in range(1,n+1):
    if(n%num==0):
      count+=1
  if(count!=2):
    print('composite')
  else:
    print('not composite')
else:
  print('not composite')

#factorial
n=int(input())
fact=1
for num in range(1,n+1):
  fact=fact*num
  print(fact)

#reverse
n=1234
rev=0
while n!=0:
  r=n%10
  rev=rev*10+r
  n=n//10
print(rev)

#palindrome
n=20
rev=0
temp=n
while n!=0:
  r=n%10
  rev=rev*10+r
  n=n//10
if(temp==rev):
  print('palindrome')
else:
  print('not palindrome')

#count
n=321456
count=0
while n!=0:
  n//=10
  count+=1
print(count)

#armstrong 3^3+7^3+1^3
n=371
temp=371
rev=0
c=len(str(n))
while n!=0:
  num=n%10
  rev=rev+num**c
  n=n//10
if(rev==temp):
  print('armstrong')
else:
  print('not armstrong')

#dis arum 135=1^1+3^2+5^3=135(by adding it will get same number)
n=135
temp=135
rev=0
c=len(str(n))
while n!=0:
  num=n%10
  rev=rev+num**c
  n=n//10
  c-=1
if(rev==temp):
  print('disrum')
else:
  print('not disarm')

#145=1!+4!+5!=145 special number
n=145
temp=145
rev=0
while n!=0:
  id=n%10
  fact=1
  for num in range(1,id+1):
    fact=fact*num
  rev+=fact
  n=n//10
if(temp==rev):
  print('special')
else:
  print('not special')

#paly prime
var=12
temp=var
rev=0
while var!=0:
  rem=var%10
  rev=(rev*10)+rem
  var//=10
if temp==rev:
  count=0
  for fa in range(1,rev+1):
    if rev%fa==0:
      count+=1
  if count==2:
    print('palyprime')
  else:
    print('not palyprime')
else:
    print('not palyprime')

#harshad no
var=123
temp=var
sum=0
while var!=0:
  id=var%10
  sum+=id
  var//=10
if temp%sum==0:
  print('harshad no')
else:
  print('not harshad no')

#binary no
num=13
rev=0
pos=1
while num!=0:
  rem=num%2
  rev=rev+(rem*pos)
  pos*=10
  num//=2
print(rev)

#binary to integer
num=1101
rev=0
pow=0
while num!=0:
  rem=num%10
  rev+=rem*(2**pow)
  pow+=1
  num//=10
print(rev)

#happyno
num=20
while num>9:
  sum=0
  while num!=0:
    id=num%10
    sum+=(id)**2
    num//=10
  num=sum
if num==1 or num==7:
  print('happy no')
else:
  print('not happy no')

#fascinating no
num='192345678'
check=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
  if str(val) not in check:
    print('NFN')
    break
else:
  print('FN')

#pronic no
var=9
n=0
while n*(n+1)<=var:
  if(n*(n+1)==var):
    print('pronic no')
    break
  n+=1
else:
  print('not pronic')

#sunny no
var=8
n=0
while n*n<=var+1:
  if(n*n==var+1):
    print('sunny no')
    break
  n+=1
else:
  print('not sunny')

def is_even(num):
  if(num%2==0):
    return True
  else:
    return False
print(is_even(20))

#prime or not
def is_prime(num):
  count=0
  for fa in range(1,num+1):
    if num%fa==0:
      count+=1
    return count==2
var=20
if is_prime(var):
  print('prime')
else:
  print('not prime')

num=100
for fa in range(2,num//2+1):
  if num%fa==0:
    print('not prime')
    break
else:
  print('prime')

def is_prime(num):
  for fa in range(2,num//2+1):
    if num%fa==0:
      return 'not prime'
  return 'prime'
print(is_prime(20))

def is_prime(num):
  for fa in range(2,int(num**(0.5)+1)):
    if num%fa==0:
      return 'not prime'
  return 'prime'
print(is_prime(97))

def is_composite(num):
  count=0
  for fa in range(1,num+1):
    if num%fa==0:
      count+=1
  return count!=2
var=100
if is_prime(var):
  print('not composite')
else:
  print('composite')

def is_fact(num):
  fact=1
  for fa in range(1,num+1):
    fact=fact*fa
  return fact
print(is_fact(5))

def prime(num,count=0):
  for fa in range(1,num+1):
    if num%fa==0:
      count+=1
  if count==2:
    return True
  return False
print(list(map(prime,range(10,41))))

def rev(num,rev=0):
  while num!=0:
    r=num%10
    rev=rev*10+r
    num=num//10
  return rev
print(list(map(rev,range(100,151))))

def sq(a):
  return a*a
print(list(map(sq,[2,3,4,5])))

print((lambda v1,v2,v3:v1+v2+v3) (11,22,33))

var=lambda v1,v2,v3:v1+v2+v3
print(var(11,22,33))

l1=[12,13,22,56]
l2=[23,45,67,45]
print(list(map(lambda v1,v2 :v1+v2,l1,l2)))

print('\n'.join(map(lambda a1:'*'*a1,range(4,0,-1))))

print('\n'.join(map(lambda sp,st:''*sp+'*'*st,range(3,-1,-1),range(1,5))))

print('\n'.join(map(lambda sp,st:''*sp+'*'*st,range(0,5),range(5,0,-1))))

print('\n'.join(list(map(lambda a1:str(a1)*a1,range(1,5)))))

print(list(map(lambda ele:ele%2==0,range(10,21))))

def linear(l,user):
  for ind in range(len(l)):
    if l[ind]==user:
      return ind
  return -1
l=[23,24,25,26,2,3,23]
user=56
print(linear(l,user))

def binary(l,user,low=0,high=len(l)-1):
    while low<=high:
        mid=(low+high)//2
        if l[mid]>user:
            high=mid-1
        elif l[mid]<user:
            low=mid+1
        elif l[mid]==user:
            return mid
    return -1
l=2,3,4,5,6
user=2
print(binary(l,user))

from functools import reduce
print(reduce(lambda fact,num:fact*num,range(1,6)))

from functools import reduce
print(reduce(lambda a,b:a+b,range(20,30)))

#bubblesort
l=[23,13,15,6,-10]
for ind1 in range(len(l)-1,0,-1):
  for ind2 in range(ind1):
    if l[ind2]>l[ind2+1]:
      l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)

#selection sort
l=[23,45,67,89,675,-1,34,5,3]
for ind1 in range(len(l)-1):
  row=ind1
  for ind2 in range(ind1+1,len(l)):
    if l[row]>l[ind2]:
      row=ind2
  l[ind1],l[row]=l[row],l[ind1]
print(l)

#quicksort
var=[23,45,67,89,675,-1,34,5,3]
def quick(var):
  if len(var)<=1:
    return var
  pivot=var[0]
  low=[var[ind] for ind in range(1,len(var))if pivot>var[ind]]
  high=[var[ind] for ind in range(1,len(var)) if pivot<=var[ind]]
  return quick(low)+[pivot]+quick(high)
print(quick(var))

print([num for num in range(10) if num%2==0])

print(['even'if num%2==0 else 'odd' for num in range(50,60)])

def quicksort(var):
  if len(var)<=1:
    return var
  pivot=var[0]
  low=[var[ind] for ind in range(1,len(var))if pivot>var[ind]]
  high=[var[ind] for ind in range(1,len(var))if pivot<=var[ind]]
  return quicksort(low) +[pivot] +quicksort(high)
var=[89,76,34,-10,7,2,8]
print(quicksort(var))

def friends(name1,name2,name3):
  print("hi",name3,name2+"," "and",name1 )
(friends("Mahesh", "Suresh", "Devesh"))

lines=5
for line in range(1,lines+1):
  for st in range(line):
    if st==0 or line==lines or st==line-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()

lines=5
for line in range(lines,0,-1):
  for st in range(line):
    if st==0 or line==lines or st==line-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()

lines=5
spaces=lines-1
for line in range(1,lines+1):
  for sp in range(spaces):
    print(' ',end=' ')
  for st in range(line):
    if st==0 or line==lines or st==line-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()
  spaces-=1

lines=5
spaces=0
for line in range(lines,0,-1):
  for sp in range(spaces):
    print(' ',end=' ')
  for st in range(line):
    if st==0 or line==lines or st==line-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()
  spaces+=1

lines=5
for row in range(lines):
  for col in range(lines):
    if row==col or row+col==lines-1:
      print('*',end =' ')
    else:
      print(' ',end=' ')
  print()

lines=5
for row in range(lines):
  for col in range(lines):
    if row==0 or col==0 or col==lines-1 or row==lines-1 :
      print('*',end =' ')
    else:
      print(' ',end=' ')
  print()

lines=5
for row in range(lines):
  for col in range(lines):
    if row==0 or col==0 or col==lines-1 or row==lines-1 or row==col==lines//2 :
      print('*',end =' ')
    else:
      print(' ',end=' ')
  print()

lines=10
for row in range(lines):
  for sp in range(row):
    print(' ',end=' ')
  for col in range(lines):
    if row==lines-1 or lines//2-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()
  spaces-=1

lines=5
for row in range(lines):
  for sp in range(lines-row):
    print(' ',end=' ')
  for col in range(2*row +1 ):
    if row==lines-1 or col==0  or  col==2*row:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()
  spaces-=1

var='onE word'
vowels='aeiouAEIOU'
for char in var:
  if char in vowels:
    print(char)

var='aaabbcccccdd'
var+=' '
count=1
res=' '
for ind in range(len(var)-1):
  if var[ind]==var[ind+1]:
    count+=1
  else:
    res+=str(count)+var[ind]
    count=1
print(res)

var='change the example'
words=var.split()
print(words)

var='change the example'
var+=' '
word=' '
l=[]
for ind in range(len(var)):
  if var[ind]==' ':
    l.append(word)
    word=''
  else:
    word+=var[ind]
print(l)

var='change the example'
words=var.split()
ans=[]
for ind in range(len(words)-1,-1,-1):
  ans.append(words[ind])
print(' '.join(ans))

L=[23,76,89,23,76,9,0,5]
user =90
def interpolation(L,user,low=0,high=len(L)-1):
    while low<=high and L[low]<=user<=L[high]:
        mid=int(low+((low-high)/(L[low]-L[high]))*(user-L[low]))
        if L[mid]>user:
            high=mid-1
        elif L[mid]<user:
            low=mid+1
        elif L[mid]==user:
            return mid
    return -1

print(interpolation(L,user))

l=[23,45,67,89,45]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)

#convert all into lower case without using lower function
s='RamLakSHiTha'
res=' '
for ind in range(len(s)):
  if 'A'<=s[ind]<='Z':
    res+=chr(ord(s[ind])+32)
  else:
    res+=s[ind]
print(res)

#convert all into upper case without using upper function
s='RamLakSHiTha'
res=' '
for ind in range(len(s)):
  if 'a'<=s[ind]<='z':
    res+=chr(ord(s[ind])-32)
  else:
    res+=s[ind]
print(res)

#convert lower into upper and vice versa
s='RamLakSHiTha'
res=' '
for ind in range(len(s)):
  if 'a'<=s[ind]<='z':
    res+=chr(ord(s[ind])-32)
  elif 'A'<=s[ind]<='Z':
    res+=chr(ord(s[ind])+32)
print(res)

s='we are dvelopers 432@1! moye'
alpha,digit,special=0,0,0
for ch in s:
  if 'a'<=ch<='z' or 'A'<=ch<='Z':
    alpha+=1
  elif '0'<=ch<='9':
    digit+=1
  else:
    special+=1
print(alpha,digit,special)

var=input()
print(var)
print(type(var))

print(list(map(int,input().split())))

l=[3,4,2,6,1,5,4]
target=8
for ind1 in range(len(l)-1):
  for ind2 in range(ind1+1,len(l)):
    if l[ind1]+l[ind2]==target:
      print(l[ind1],l[ind2])

num=int(input())
while num!=0:
  rem=num%10
  if rem>1:
    for fa in range(2,rem//2+1):
      if rem%fa==0:
        break
    else:
      print(rem)
  num//=10

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print([l1[ind]+l2[ind] for ind in range(len(l1))])

def fib(n):
  a,b=0,1
  for _ in range(n):
    print(a,end='')
    a,b=b,a+b
print(fib(10))

class bike:
  pass
r15=bike()
print(r15)

class sbi:
  bname='somala'
  ifsc='sbin0001'
  roi=8
ram=sbi()
print(sbi.ifsc)
print(ram.bname)
ram.roi=5
print(ram.roi)

class SBI:
  def __init__(self):
    print('constructor')
ram = SBI()
sam=SBI()

class SBI:
  bname='somala'
  ifsc='sbin0001'
  roi=8

  def __init__(self,name,mbno):
    self.name=name
    self.mbno=mbno
c1=SBI('ram',93924467876)
c2=SBI('sam',9876543210)
print(c1.name,c1.mbno)

class m12:
  time='2.30'
  course='python'
  def __init__(self,name,mbno,gender):
    self.name=name
    self.mbno=mbno
    self.gender=gender
  def details(self):
    print(f'name:{self.name}')
    print(f'mbno:{self.mbno}')
    print(f'gender:{self.gender}')
st1=m12('ram',9876543210,'male')
st2=m12('lucky',1234567890,'female')
st1.details()
st2.details()

class ourbank():
  nob=1
  ifsc='obi000543'
  def __init__(self,name,aadhar,mno,bal):
    self.name=name
    self.aadhar=aadhar
    self.mno=mno
    self.bal=bal
  def deposit(self):
    amount=int(input('enter the amount'))
    self.bal+=amount
    print('amount credited sucessfly...')
    print(f'available balane is{self.bal}')
  def withdraw(self):
    amount=int(input('enter the amount'))
    if amount<=self.bal:
      self.bal-=amount
      print('amount debbited sucessfully.....')
      print(f'avalliable balance is {self.bal}')
    else:
      print('insufficient funds...')
us1=ourbank('ram',1213454566,9876543,10000000)
us2=ourbank('sam',8777678999,123456789,2000000)
us2.withdraw()
us1.deposit

#to print consonants
s=input()
vowels='aeiouAEIOU'
res=''
for ch in s:
    if ch not in vowels:
        res+=ch
print(res)

# program to convert upper into lower without using inbuilt methods
def convert_to_lower(s):
  res=''
  for ch in s:
    if 65<=ord(ch)<=90:
      res+=chr(ord(ch)+32)
    else:
      res+=ch
  return res
s='HELLO WORLD'
print(convert_to_lower(s))

def convert_to_upper(s):
  res=''
  for ch in s:
    if 97<=ord(ch)<=122:
      res+=chr(ord(ch)-32)
    else:
      res+=ch
  return res
s='ram'
print(convert_to_upper(s))

def special(s):
  for ch in s:
    if not('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
      print(ch,end='')
s='ram123@  !#'
special(s)

def special(s):
  characters=[]
  for ch in s:
    if not ch.isalnum():
      characters.append(ch)
  print(' '.join(characters))
s='lakshi ^ tha 123'
special(s)

#file handling to count no of lines
fobj=open(r'/content/lakshi.txt')
a=fobj.readlines()
print(len(a))

fobj=open(r'/content/lakshi.txt')
count=0
for _ in fobj:

  count+=1
print(count)

#no of words
fobj=open(r'/content/lakshi.txt')
count=0
for line in fobj:
  count+=len(line.split())
print(count)

#no of characters
fobj=open(r'/content/lakshi.txt')
count=0
for line in fobj:
  line=line.strip("\n")
  count+=len(line)
print(count)

fobj=open(r'/content/lakshi.txt')
vowels='aeiouAEIOU'
count=0
for line in fobj:
  for ch in line:
    if ch in vowels:
      count+=1
print(count)

#special characters
fobj=open(r'/content/lakshi.txt')
count=0
for line in fobj:
  for ch in line:
    if not('A'<=ch<='Z' or 'a'<=ch<='z'or '0'<=ch<='9'):
      count+=1
print(count)

import json
json.dumps(3)
json.dumps(4.2)
json.dumps(True)
#json.dumps(6+6j) complex error

fobj=open(r'/content/lakshi.txt')
count=0
for line in fobj:
  line=line.split('\n')
  count+=len(line)

num = 11
print('not prime number' if list(filter(lambda fa: num % fa == 0, range(2, num // 2 + 1))) else 'prime')

l = []
for num in range(100, 1001):
    if not list(filter(lambda fa: num % fa == 0, range(2, num // 2 + 1))):
        l.append(num)
print(l)

import json
d={'ram':'lakshi','thukaram':'lakshitha'}
with open('convert.json','w') as fobj:
  data=json.dumps(d,indent=3)
  fobj.write(data)

import json
d={'ram':'lakshi','thukaram':'lakshitha'}
with open('convert.json','w') as fobj:
  json.dump(d,fobj,indent=3)

with open('convert.json','r') as fobj:
  data=fobj.read()
  print(json.loads(data))

with open('convert.json') as fobj:
  print(json.load(fobj))

#match it search at the starting of the string
import re
s='i love ram lakshitha'
re.match('i',s)

re.match('z',s)

#search search any character in string
s='i love ram lakshitha'
re.search('a',s)

s='i love ram lakshitha'
re.findall('a',s)

s='i love ram lakshitha'
re.findall('x',s)

re.split('a',s,1)

re.sub('a','o',s)

s='i love ram lakshitha'
re.subn('a','o',s)

re.finditer('a',s)

list(re.finditer('a',s))

a=re.compile('a')
a.findall(s)

s='123rhnmnud\nhbgvbjvk2i;ve\n'
re.findall('.',s)

re.findall('^123',s)

re.findall('abc$',s)

re.findall(';ve\n$',s)

s='goood night ram'
re.findall('i+',s)

re.findall('a?',s)

re.findall('o?',s)

re.findall('o?',s)

re.findall('o{3}',s)

re.findall('a|o',s)

r='abcDtsdkuerjhi;/DGB.n132763E6803 08IE1NF'
re.findall('[arn]',r)

re.findall('[^ab]',r)

re.findall('[a-z]',r)

re.findall('[A-Z]',r)

re.findall('[0-9]',r)

a='kjdchvb +$^&U*'
re.findall('+',a)

re.findall('[+]',a)

#phone number is valid or not
import re
s='+91-9392447054'

if re.match('[+]91 [6-9][0-9]{9}$|[+]91-[6-9][0-9]{9}$',s):
  print('valid')
else:
  print('invalid')

# email is valid or not
s='ramlakshitha1989.@gmail.com'
if re.match('\w*[.]?\w*@gmail[.]com$',s):
  print('valid')
else:
  print('invalid')

def a():
  a=20
  yield a
  a+=5
  yield a
obj=a()
print(next(obj))
print(next(obj))

def a():
  a=20
  yield a
  a+=5
  yield a
obj=a()
print(list(obj))

#fibonacci using recursions
def fib(pos):
  if pos==1 or pos==2:
    return pos-1
  return fib(pos-1)+fib(pos-2)
pos=6
print(fib(pos))

#fibonacci using range
def fib(pos):
  a=0
  b=1
  for _ in range(pos):
    c=a+b

    yield c
    a,b=b,c
pos=7
obj=fib(pos)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

l=[23,3,4]
print(iter(l))

l=[23,3,77]
obj=iter(l)
print(next(obj))
print(next(obj))
print(next(obj))

# decorator
def outer(arg):
  print(arg)
  def inner():
    arg()
  return inner
@outer
def function():
  print('inside function')

def outer(arg):
  def inner(a,b):
    if a<0:
      a=a*(-1)
    if b<0:
      b=b*(-1)
      arg(a,b)
  return inner
@outer
def add(a,b):
  print(a+b)
add(-2,-3)

#program to find power of 2
def is_power(n):
  if n<=0:
    return false
  else:
    return n&(n-1)==0
n=int(input())
if is_power(n):
  print('is power of n'.format(n))
else:
  print('is not power of n'.format(n))

def merge(s1,s2):
    result=""
    i=0
    while  i<(len(s1)) or i<(len(s2)):
        if(i<len(s1)):
            result+=s1[i]
        if (i<len(s2)):
            result+=s2[i]
        i+=1
    return result

s1="hello"
s2="hi"
print(merge(s1,s2))

username=input()
password=input()
try:
    if password=='_123':
        print('login sucessfull')
    else:
        raise Exception
except Exception:
    print('invalid')

def add(a,b):
  try:
    return a+b
  except Exception:
     return('invalid')
print(add(1,22))
print(add(1,'a'))

def singleton(arg):
    l=[]
    def inner():
        if len(l)==0:
            a=arg()
            print(a)
            l.append(a)
        else:
         pass
    return inner
@singleton
class pvr:
    def __init__(self):
        print('object created')
obj1=pvr()
obj2=pvr()

def ispalindrome(s):
  return s==s[::-1]
s='hello'
print(ispalindrome(s))

def ispalindrome(s):
  return s==s[::-1]
s='first'
ans=ispalindrome(s)
if ans:
  print('string is palindrome')
else:
  print('string is not palindrome')

def reverse(s):
  s=s[::-1]
  return s
s='geeks for geeks'
print(reverse(s))