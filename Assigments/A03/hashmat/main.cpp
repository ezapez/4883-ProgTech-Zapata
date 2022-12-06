#include <iostream>
using namespace std;


int main() {
  long long int a =0;
  long long int b =0;

  while (cin >> a >> b){
    cout << abs(a-b) << endl;
  }

  return 0;
}