#Print all numbers between 1 and 20
for i in range(1,21):
  print(i)

#Print all odd numbers between 1 and 20
for i in range(1,21):
  if i%2!=0:
    print(i)

#Check if a number is even or odd
num = 8
if num%2 == 0:
  print("even")
else:
  print("odd")

#Print the sum of numbers from 1 to 10
n = 0
for i in range(1,11):
  n=n+i
print(n)

#Print multiplication table of a number (e.g., 5)
num=4
for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

#Even numbers from 1–50
for i in range(1,51):
  if i%2 == 0:
    print(i)

#Sum of only even numbers
total = 0
for i in range(1,51):
  if i%2 == 0:
    total = i+total
print(total)




