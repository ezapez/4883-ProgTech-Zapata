import sys

# Read the first line of input
line = input()
### read each line untill it reaches  0 0 0
### to end the program
while line != "0 0 0":
  # Split the line into the three sides of the triangle
  a, b, c = map(int, line.split())
  ## printing to see if it outputing 
 ## print(a)
 ## print(b)
 ## print(c)
  
  # Compute the square of the length of the hypotenuse and the sum of the squares of the lengths of the other two sides
  # resourced used 
  #https://www.sololearn.com/discuss/2511631/pythagoras-theorem-else-statements-python
  #https://www.instructables.com/Python-Programming-Functions-Pythagorean-Theorem/
  #https://www.geeksforgeeks.org/find-the-hypotenuse-of-a-right-angled-triangle-with-given-two-sides/
  ### find the largest intger gets the pow 10^2 = 100
  hypotenuse_squared = max(a, b, c) ** 2
  ##print( hypotenuse_squared)
  ### times all sides and adds them together 
  others_squared = a ** 2 + b ** 2 + c ** 2 - hypotenuse_squared
  ### 200 - 100 
  ### 6^2 36 + 8^2 64 + 10^2 100 = 200
  ### 200 - 100
  ##print( others_squared)
  # If the square of the length of the hypotenuse is equal to the sum 
  ## of the squares of the lengths of the other two sides
  # it means the triangle is a right triangle
  ##
  if hypotenuse_squared == others_squared:
      print("right")
  else:
      print("wrong")
  ## keep going through the input untill it reaches end 
  line = input()