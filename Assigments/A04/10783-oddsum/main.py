
### question 
##Given a range [a, b], you are to 
##find the summation of all the odd integers in this range. 
##For example,
##the summation of all the odd integers 
##in the range [3, 9] is 3 + 5 + 7 + 9 = 24.

import sys
## how to input file 
## used to 
T = int(input())
## looping to from 1 to input 
for i in range(1, T+1):
### grabs input to be placed into a,b
  a = int(input())
  b = int(input())
  odd_sum = 0

  for n in range(a, b+1):
    if n % 2 == 1:
      ## count the amount of 
      odd_sum += n
  ### prints out the odd sum and case number 
  print(f"Case {i}: {odd_sum}")