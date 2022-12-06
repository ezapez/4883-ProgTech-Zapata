import sys 
### to input files via terminal
t =int(input())


### loop 
for i in range(t):
  ### map to split the input to compare
  a, b = map(int, input().split())
## compare what is bigger or smaller or equal
### if statments to compare 
  if a > b:
    print(">")
  elif a < b:
    print("<")
  else:
    print("=")