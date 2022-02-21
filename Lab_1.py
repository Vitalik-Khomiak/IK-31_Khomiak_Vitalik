from datetime import date
from dateutil import parser

print('HELLo World!')
print('Please, enter your name:')
input1 = input()
print('HELLo,',input1,'!')
a = len(input1)

fact=1 
for i in range(2,a+1): 
  fact=fact*i 
print ("Your name has",a,"letters. ",a,'! = ',fact)

date = parser.parse(input("Please, enter your birth date in format (DD.MM.YYYY):"))
days_in_year = 365.2425   
today =  date.today()
age = int((today - date).days / days_in_year)
day = today - date

print("Today is",today,', you are',age,'year (',str(day.days),') old.')
