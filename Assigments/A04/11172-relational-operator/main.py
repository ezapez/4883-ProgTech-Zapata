# ### keeps getting error end of file
# while True:

#   ### map to split the input to compare
#   a,b = map(int,input().split())

#   # ## compare what is bigger or smaller or equal
#   # ### if statments to compare
#   if a > b:
#     print(">")
#   elif a < b:
#     print("<")
#   else:
#     print("=")

#   t -= 1;





import sys
# ### to input files via terminal

#resource to fix it
#https://www.educba.com/python-eoferror/
#https://stackoverflow.com/questions/42891603/how-to-remove-eoferror-eof-when-reading-a-line
t = int(input())

while True:
  try:
    ### map to split the input to compare
    a,b = map(int,input().split())

    # ## compare what is bigger or smaller or equal
    # ### if statments to compare
    if a > b:
      print(">")
    elif a < b:
     print("<")
    else:
      print("=")

    t -= 1;
  except:
    break
