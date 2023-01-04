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