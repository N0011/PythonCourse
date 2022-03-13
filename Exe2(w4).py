max_value = int(input('Display primes up to what value? '))
value = 2 
while value <= max_value:
  is_prime = True 
  trial_factor = 2
  while trial_factor < value:
       if value % trial_factor == 0:
          is_prime = False 
          break
       trial_factor += 1
  if is_prime:
       print(value, end='') 
  value += 1
print() 

#Display prices up to what value? 90 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89