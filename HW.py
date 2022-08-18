print(sum(range(1,10)))
########################################################################
print(sum(range(2,17,2)))
#####################################################################
print(sum(range(1,16,2)))
#############################################################
lion = lambda x,y,z: range(x,y,z)
#print(sum(range('x,y,z')))
###################################################
#multiplication table
i =2
while i in range(2,22):
    print(i, end='')
    i = i+2
#########################################################
num = 10
num =int(input('Display multiplication table of:'))
for i in range(1,11):
    print(num*i)
####################################################
s = '901578559885555555'
if s.isdigit():
    print(len(s))
#################################################
n = 10

n = (input('enter the number:'))
print(n[0],n[-1])
#################################################
n = 456789
n = (input('enter the number:'))
n1=int(n[0])
n2=int (n[-1])
print(int(n1*n2))
#############################################
m= int(input('Enter a number:'))
tot = 1
while m>0:
    dig = m%10
    tot = tot*dig
    m = m//10
    print('the total sum of digits i:',tot)
############################################################
k = (input('Enter a number and make reverse:'))
k [-1]
print(k[::-1])
##################################################################
k = (input('Enter a number and check whether is palindrome:'))
if k[::-1] == k:
    print('entered nuber is palindrome')
else:
    print('the number is not palindrome')
#############################################################################################
p = int(input('Enter a number and check whether is prime:'))
n = int(num)
if p % n != 0:
    print('entered nuber is not prime')
else:
    print('entered nuber is  prime number')