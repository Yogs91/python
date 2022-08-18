def sum (a,b):
    print(a+b)
sum(10,20)
########################################################
def div (x,y):
    print(x/y)
div(100,10)
#########################################################
def info (name,age):
 print('your name is',name)
 print('your age is', age)
info(name='suhas', age= 24)
#############################################
def max (a,b,c):
    if a > b or c:
        return a
    elif b > a or c:
        return b
    else:
        return c
    result = max(1,2,3)
    if result == a:
        print(a is max)
    elif result == b:
        print(b is max)
    else:
        print(c is max)
 ############################################################################
f = open('a.txt')
print(f.readline(5))
print(f.readline(5))
print(f.readline(5))
print(f.readline())
print(f.readline())
print(f.read(20))
##################################################################################
f = open('a.txt')
print(f.readline())
print(f.readline())
print(f.readline(3))
print(f.readline())
print(f.readlines())
print(f.readlines())
##################################################################

f = open('a.txt')
data = f.read()
for i in data:
    print(i)
#################################################################
f = open('a.txt')
data = f.readline()
for i in data:
    print(i)
####################################################################
f = open('a.txt')
data = f.readlines()
for i in data:
    print(i)
#####################################################################
f = open('a.txt')
print(f.read(18))
print(f.read())
for i in range(3):
    print(f.read())
########################################################################
f = open('a.txt')
for i in range(3):
    print(f.readline())
##########################################################################
f = open('a.txt')
for i in range(5):
    print(f.readlines())
###########################################################################
f = open('b.txt', mode='w')
print(f)
print(f.writable())
f.write('ksa winner is shivaji')
f.write('km runner up is mandal')
f.write('shahu winner is shivaji')
f.write('netaji winner is mandal')
print(f.writable())
f.write('ksa winner is shivaji\nkm runner up is mandal\nshahu winner is shivaji\nnetaji winner is mandal')
##############################################################################################################
f.writelines(['ksa winner is shivaji\nkm runner up is mandal\nshahu winner is shivaji\nnetaji winner is mandal'])
###################################################################################################################
f = open('b.txt', mode='w')
print(f.writable())
f.writelines(['name is yogesh\n','age is 32\n','place is kolhapur'])
########################################################################################################
f= open('b.txt')
print(f.tell())
print(f.read(100))
print(f.tell())
########################################################################################################
f= open('b.txt')
f.seek(12)
print(f.read())
#####################################################################################################
f= open('c.txt', mode='w')
f.seek(10)
print(f.read())





