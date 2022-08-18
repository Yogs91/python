import csv
f = open('sample.csv', 'w', newline='\n')
wr = csv.writer(f)
print(wr)
wr.writerow(['Name','Age','Salary'])
wr.writerow(['yogesh','32','25000'])
wr.writerow(['varad','8','10000'])
wr.writerow(['adhiraj','1','5000'])
#############################################################################
import csv
f= open('test.csv', 'w',newline='\n')
wr = csv.writer(f)
n= int(input('How many records you want to add?'))
for i in range(n):
    nm = input('Enter the name of student:')
    ag = int(input('Age of a student:'))
    wr.writerow(['nm','Age'])
##############################################################################
import csv
f2= open('sample.csv')
rd = csv.reader(f2)
print(rd)
print(list(rd))
###################################################
#WAP to priny all even from 1-10
num = 1
while num < 11:
    print(num+1)
    num += 2
#######################################################################################
#1WAP to priny all natural numbers  from 1-n
i= 1
while i >=1 :
    print(i, end= ''   )
    i=i+1
###########################################################################################

