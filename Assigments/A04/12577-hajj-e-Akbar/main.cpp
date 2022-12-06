/*
  plan:
  1.  while loop a string to get inputs
  2. if statments when a string is input 
     output the required statment
    keep count of the cases 
  3. when the * is inputed stop program a
*/
#include <string> // for string class
#include <iostream>
using namespace std;
int main() {
  string input;
  int count = 0;
  while( cin >> input )
    {
      // if input is not equal to * run these if statments untill * is inputed:
      if( input != "*")
      {
        count++;
        if(input == "Hajj")
        {
          cout << "Case " << count << ": " << "Hajj-e-Akbar" << endl;
        }
         if(input == "Umrah")
        {
          cout << "Case " << count << ": " << "Hajj-e-Asghar" << endl;
        }
      }
      else
      {
        return 0;
      }
    }
  return 0;
  
}