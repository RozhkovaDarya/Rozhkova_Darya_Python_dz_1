items = []
for i in range(1,1000,2):
  items.append(i**3)
  
#print(items)

for i in range(len(items)):
  temp = str(items[i])
  sum_temp = 0
  for j in temp:
    sum_temp += int(j)
  if sum_temp % 7 == 0:
    print (sum_temp, end = ', ')

print('\n')


new_items = []

for i in items:
  new_items.append(i + 17)

#print(new_items)

for i in range(len(new_items)):
  temp = str(new_items[i])
  sum_temp = 0
  for j in temp:
    sum_temp += int(j)
  if sum_temp % 7 == 0:
    print (sum_temp, end = ', ')

