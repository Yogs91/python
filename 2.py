#Write a Python program to extend a list without append
k = [1,2,3,4,5]
l = [6,7,8,9,10]
l[:0] = k
print(l)
################################################
n= [1,2,3,4,5,6]
n[0]=n[2]
n[1]= n[3]
print(n)
#################################################
n= [1,2,3,4,5,6]
print(max(n))
#################################################
a = [10,30,20,40,60,75,80]
max = a[0]
for i in a:
    if i > max:
        max = i
print(max)
#######################################################
num =int(input('Display multiplication table of:'))
for i in range(1,11):
    print(num*i)
####################################################
n = int(input('Enter a Number :'))
for i in range(2,n):
    if n % i == 0:
        print(n, 'is not a prime number')
        break
else:
     print(n , 'is prime')
##############################################################################
k = [1,2,3,4,5]
l = [6,7,8,9,10]
m = l[::-1]
n= sum(k+m)
print(n)