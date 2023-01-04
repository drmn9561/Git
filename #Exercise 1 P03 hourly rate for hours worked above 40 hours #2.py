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