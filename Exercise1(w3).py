salary = float(input("Enter the salary? "))

      
if salary <= 1000:
       tax = 0
elif salary <= 2500:
       tax = (salary - 1000) * 0.10
elif salary <= 4000:
       tax = (salary - 2500) * 0.15 + 150
elif salary <= 6000:
       tax = (salary - 4000) * 0.20 + 375
elif salary <= 8000:
       tax = (salary - 6000) * 0 + 525
else:
    taxt = (salary - 8000) * 0.30 + 525

print(salary)