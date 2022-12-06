import sys
### keeps getting error end of file 
# # Read the input one line at a time
# line = input()
# while line:
#     # Split the line into two numbers
#     n, k = map(int, line.split())

#     # Compute the maximum number of cigarettes that Peter can have
#     cigarettes = n + (n - 1) // (k - 1)

#     # Print the result
#     print(cigarettes)

#     # Read the next line of input
#     line = input()

#resource to fix it 
#https://www.educba.com/python-eoferror/
#https://stackoverflow.com/questions/42891603/how-to-remove-eoferror-eof-when-reading-a-line
while True:
  try:
   ## Split the line into two numbers
    n, k = map(int, input().split())

    # Compute the maximum number of cigarettes that Peter can have
    cigarettes = n + (n - 1) // (k - 1)

    # Print the result
    print(cigarettes)
    n-=1
  except:
    break

    

