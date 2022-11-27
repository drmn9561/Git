# Python exercise Total 
#Comparison Operators
x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
   print('Greater than 4')
if  x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')

    #Comput Grosspay
hrs=input('PLZ Enter Hours:')
rte=input('PLZ Enter Rate:')
grosspay=(float(hrs)*float(rte))
print(grosspay)

#Exercise 1 P03: hourly rate for hours worked above 40 hours
hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
if hours <= 40:
  pay = hours * rate
else: 
  pay = (40*10)+(hours-40)*(1.5*rate)
print (pay)

#Exercise 1 P03: hourly rate for hours worked above 40 hours
hours = input('Enter Hours:')
rate = input('Enter Rate:')
hours=float(hours)
rate=float(rate)
if hours <= 40:
 pay = hours * rate
else: 
 pay = (40*10)+(hours-40)*(1.5*rate)
print (pay)

#Exercise 2: pay program using try and except - program handles non-numeric input gracefully
h = input('Enter Hours:')
r = input('Enter Rate:')
try:
  hours = float(h)
  rate = float (r)
  if hours <= 40:
    pay = hours * rate
  else:
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
  print ('Pay =' , pay)
except:
    print('Error, please enter numeric input')

    #Functions
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fa':
        print('salam')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('fa')
greet('es')
greet('fr')

#Multi-way Decisions
x=4
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 : 
        print('Less than 100') 
print('All done')

#One-Way Decisions
x = 5
print('Before 5')
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print("All Done")

#Order of Evaluation
x = 1 + 2 ** 3 / 4 * 5
print(x)

#Return Value
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')

#String Conversions
a='123'
print(a)
print (type(a))
f=int(a)
print(f)
print (type(f))

#Two-way Decisions
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')

#Type Conversions
i=42
print (i)
print(type(i))
f=float(i)
print(float(i))
print(type(f))

#Types of Numbers
x=1
print (type (x))
temp = 98.6
print (type (temp))