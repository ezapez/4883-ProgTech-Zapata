## code was written in class with prof griffen
t = int(input())
while t:
  ### list to split the inputs 
  m, n = list(map(int, input().split()))
  
  
  n = int(n)
  m = int(m)
  
  mm = m % 3
  nn = n % 3
  
  
  print(int(((n-nn) * (m-mm))/9))
  t -= 1

