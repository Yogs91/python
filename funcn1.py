s = lambda x: x + 100
print(s(50))
####################################################################

sq = lambda n: n*n
print(sq(5))
###############################################################
sample = lambda name,branch='BOI':name+' '+branch
print(sample('yogesh'))
######################################################
sub = lambda x: x-50
print(sub(71))
##############################################33
acc = lambda name, branch,ifsc : name + branch + ifsc
print(acc('yogs', 'kolhapur', '77590'))
##########################################################
kacc = lambda name, branch,ifsc : name + branch + ifsc
print(kacc(name='yogs', branch = 'kolhapur', ifsc= '77581'))
###########################################################
given = lambda n : n+15
print(given(25))
##############################################################
mul = lambda x,y : x*y
print(mul(10,20))
#############################################################
num = lambda m : m.aisdigit()
print(mul(10,50))
#################################################################
def assemble(x,y):
    print('x assemble in y')
assemble(10,20)
#################################################################
p ='1234abcd'
print(p[::-1])
################################################################
from functools import reduce
k =[8,2,3,-1,7]
mul = print(reduce(lambda x,y: x*y,k))
###############################################################
from functools import reduce
l =[8,2,3,0,7]
add = print(reduce(lambda x,y: x+y,l))
