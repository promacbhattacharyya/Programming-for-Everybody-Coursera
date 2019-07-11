## Assignment 1: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 

hours = input('Enter the hours worked: ')
rate = input('Enter the rate: ')
h = float(hours)
r = float(rate)
pay = (h*r)
print('Your pay is: $',pay)

## Assignment 2: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
## Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
hours = input('Enter the hours: ')
rate = input('Enter the rate/hour: ')
h = float(hours)
r = float(rate)
if h<=40:
    pay = (h*r)
else:
    exhour = (h-40)
    newrate = (r*1.5)
    pay = ((40*r)+(exhour*newrate))
print('Gross Pay: ',pay)

## Assignment 3: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
## Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
hours = input('Enter the hours: ')
rate = input('Enter the rate/hour: ')
h = float(hours)
r = float(rate)
def computepay():
    if h<=40:
        pay = (h*r)
    else:
        exhour = (h-40)
        newrate = (r*1.5)
        pay = ((40*r)+(exhour*newrate))
    return(pay)
print ('Your pay is: ', computepay())

## Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.  
## If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 

largest = None
smallest = None
while True:
  try:
    numberinput = input('Enter an integer ')
    if numberinput == 'done':
      break
    number = int(numberinput)
    if smallest is None:
        smallest = number
    elif smallest > number:
        smallest = number
    elif largest is None:
        largest = number
    elif largest < number:
        largest = number
  except:
    print ('Check value')
print ('Largest: ', largest, 'Smallest: ', smallest)




























