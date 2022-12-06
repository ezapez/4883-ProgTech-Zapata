/*
test case:
  at most 10 words in the input   
  all lowercase 
  all have same lenght
plan:
1.while loop to read number of inputs
2. read each string with a char limit of 10
3. if statments:
  check the first letter of each input:
  if the letter o then ouput one
  else if 
      letter is t check the lenght of the string:
      two = 3, three = 5

4. output the number 

*/

   // char fch = input.front();
   //      if(fch == 'o')
   //      {
   //        cout << "1" << endl;
   //      }
   //      else{
   //        return 0;
   //      }

#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;
int main() {
  int inputs;
  int i = 0;
  
  cin >> inputs;

  while( i < inputs)
    {
      // numbers of char 
      char nums[10];
      cin >> nums;

      
      if(strlen(nums) == 5)
      {
        cout << "3" << endl;
      }
        // one
        // two
      else 
      {

        // count the number of char in one
        // 
        int count = 0;
        if(nums[0] == 'o')
         {
           count ++;
         }
        if( nums[1] == 'n')
        {
          count++;
        }
        if( nums[2] == 'e')
        {
          count++;
        }

        if(count >= 2)
        {
          cout << "1" << endl;
        }
        else if( count < 2)
        {
          cout << "2" << endl;
        }
          
      }
      
      


      i++;
    }
  
  return 0;
}