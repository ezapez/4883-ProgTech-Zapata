import sys
t = int(input())

### looping the in range 
for i in range(t):
  n = int(input())
  ## finds 
  result = abs((n * 567 // 9 + 7492) * 235 // 47 - 498)
  ## finds the absoult value 
  tens_digit = abs((result // 10) % 10)
## prints the reluts
  print(tens_digit)

