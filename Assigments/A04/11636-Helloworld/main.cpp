#include <cmath>
#include <iostream>

using namespace std;
/*
plan
Given the number of “Hello World!”
lines you need to print, you will have to find out the minimum number of pastes
required to make that program from the origin program shown in Figure 1.

1:hello world

2:
hello world
hello world

3:
hello world
hello world
hello world
hello world

4:
hello world
hello world
hello world
hello world
hello world
hello world
hello world

5.
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world

test case:
  N  less 10001



1. see pattern  
2. while loop
    cin  number of inputs
3. test case to stop program when n is negative 
4. while loop to keep liooping sum of hello worlds
  untill it reaches nums
  count number of copy paste 
5. print the case and count of copy paste



*/
int main() {
  int n = 0; 
  int count = 0;
  int nums = 0;
  int sum = 1; 
  while(cin >> nums)
    {
      if(nums > 0)
      {

        n++;
        while(sum < nums)
          {
            sum+=sum;
            count++;
          }
        cout << "Case " << n << ": " << count << endl;
        sum = 1;
        count = 0;
      }
      

      
    }
  
  return 0;
}