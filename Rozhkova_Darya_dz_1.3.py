number = int(input())

percent = {
  1: 'процент',
  2: 'процента',
  3: 'процентов'
 }

if number % 10 == 1:
  print(f'{number} {percent[1]}')
  
elif 1 < (number % 10) < 5:
  print(f'{number} {percent[2]}')
  
  
elif 5 <= (number % 10) < 21:
  print(f'{number} {percent[3]}')
  
else:
  print(f'{number} {percent[3]}')

