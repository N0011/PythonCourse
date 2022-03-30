l=[]
number=0
count = 0
sum = 0.0
while number >= 0 :    
    number=int(input('Enter your Number: '))
    l.append(number)
    sum = sum + number
    count += 1
if count < 0:
  print("Input some numbers")
else:
  print("Average , Sum , maximum and minimum of the above numbers are: ", sum /count ,",", sum ,",", max(l) , "," , min(l))