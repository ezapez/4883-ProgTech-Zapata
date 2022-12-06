import sys

# Read the number of test cases
cases = int(input())

# For each test case
for t in range(1, cases + 1):
  # Read the salaries of the three employees and sort by lowest and highest
  salaries = sorted(list(map(int, input().split())))

  # Calculate the difference between the highest and lowest salary
  diff = salaries[-1] - salaries[0]

  # If the difference is less than or equal to 1000, output the salary of the person who survives
  if diff <= 1000:
    print(f"Case {cases}: {salaries[1]}")
  # Otherwise, output the salary of the person who gets the highest salary
  else:
    print(f"Case {cases}: {salaries[-1]}")