## example of type() function
x = 2
type('x')

## example of type conversion (using int to convert a string to integer)
abcde = '12345'
pb = int(abcde)
x = pb+1
print (x)

## Example of input: Conversio using input
rupee = input('Indian Currancy? ')
dollar = float(rupee)*75
print ('USD: ', dollar)

## Example 1 with if and else
number = input('Enter the number: ')
x = float(number)
if x>1:
    print('bigger')
else:
    print('smaller')

## Example 2 with elif
number = input('Enter the number: ')
x = float(number)
if x==20:
    print('same')
elif x<15:
    print('smaller')
else:
  print('LARGE')
print('exit')

## Example 3 with try and except: When the first clause (try) fails code jumps to the except clause and instead of failing it continues
name = input('What is your name')
try:
    nameint = int(name)
except:
    nameint = 'string'
print (nameint)

## Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
inpscore = input('Enter the Score: ')
score = float(inpscore)
if score>1:
    print ('Check Value')
elif score<0:
    print ('Check Value')
else:
    if score>= 0.9:
        grade = 'A'
    elif score>= 0.8:
        grade = 'B'
    elif score>= 0.7:
        grade = 'C'
    elif score>= 0.6:
        grade = 'D'
    elif score< 0.6:
        grade = 'F'
    print ('Grade: ', grade)
    
## Example of Stored and Reuse (use of "def")
askname = input('What is your Name? ')
def name():
    print ('Hello', askname)
inpscore = input('Enter the Score: ')
score = float(inpscore)
if score>1:
    name()
    print ('Check Value')
elif score<0:
    name()
    print ('Check Value')
else:
    if score>= 0.9:
        grade = 'A'
    elif score>= 0.8:
        grade = 'B'
    elif score>= 0.7:
        grade = 'C'
    elif score>= 0.6:
        grade = 'D'
    elif score< 0.6:
        grade = 'F'
    name()
    print ('Your Grade is: ', grade)    
    
## Max and min example: they can be used for numbers as well as strings: For strings,(" ") space is the minimum value if present
big = max('zabrisky')
little = min('zabrisky')
print(big)
print(little)

## Example of def: here the code is stored using def in grade; later when a value is given it reads from def
def grade(score):
    if score>= 0.9:
        print ('Grade: A')
    elif score>= 0.8:
        print ('Grade: B')
    elif score>= 0.7:
        print ('Grade: C')
    elif score>= 0.6:
        print ('Grade: D')
    elif score< 0.6:
        print ('Grade: F') 
        
## Example of while and break
while True:
    hours = input('Enter the hours: ')
    rate = input('Enter the rate/hour: ')
    h = float(hours)
    r = float(rate)
    exhour = (h-40)
    newrate = (r*1.5)
    ExtraPay = ((40*r)+(exhour*newrate))
    if h<=40:
        break
    print ('Your pay1 is: ', ExtraPay)   
RegularPay = (h*r)    
print ('Your pay2 is: ', RegularPay)

## Example of "continue" and "break"; However this is an indefinite loop
## Need to find out how to break the loop
## break skips out of the loop and continue skips to the starting of the loop
while True:
    inpscore = input('Enter the Score: ')
    score = float(inpscore)
    if score>1:
        continue
    if score<0:
        continue
    if score>= 0.9:
      print ('grade = A')
    elif score>= 0.8:
      print ('grade = B')
    elif score>= 0.7:
      print ('grade = C')
    elif score>= 0.6:
      print ('grade = D')
    elif score< 0.6:
      print ('grade = F')
      break
print('All done!')

## Finding the larget so far number in a set of positive numbers using for
x = 0
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    if i>x:
        x=i
print ('largest in the set: ',x) 

## Counting using 'for'
x = 0
letters = ['A,', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in letters:
    x=x+1
print('Count: ',x)

## Addition using loop
sum = 0
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    sum=sum+i
    print('Running Total: ',sum)
print ('sum: ',sum)

## Average using loop
sum = 0
count = 0
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    sum=sum+i
    count = count+1
avg = (sum/count)
print ('Average: ',avg)

## Filtering in a loop
count = 0
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    if i>15:
        count=count+1
        print ('larger than 15: ',i)
print (count, 'numbers are larger than 15')      

## Finding a particular value using True-false (boolean variable)
## Example 1
condition = False
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    if i!=14:
        condition = True
    else:
      print('14 is present in the loop')
print ('Done ')  

## Example 2
condition = False
count = 0
numbers = [10,15,20,50,60,3,5,8, 20,40, 70,80, 100, 20]
for i in numbers:
    if i==20:
        condition = True
        count = count+1
print('Number of 20 in the set', count)

## Using "None" to find out the smallest number
smallest = None
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    if smallest is None:
        smallest = i
    elif i<smallest:
      smallest=i
print ('smallest number is:', smallest)

## Using "None" to find out the largest number
largest = None
numbers = [10,15,20,50,60,3,5,8]
for i in numbers:
    if largest is None:
        largest = i
    elif i>largest:
      largest=i
print ('largest number is:', largest)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
