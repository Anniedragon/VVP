//lab 2, task 1.1
#include <iostream>
using namespace std;
int main() {
 float N;
 cout << "Enter N" << endl;
 cin >> N;
 int i;
 float st;
 st = 1;
 for (i = 1; i <= N; i++) {
  st = st * 2;
 }
 cout << st << endl;
 return 0;
}

//lab 2, task 1.2
#include <iostream>
using namespace std;
int main() {
 float N;
 cout << "Enter N" << endl;
 cin >> N;
 int i;
 float F;
 F = 1;
 for (i = 1; i <= N; i++) {
  F = F * i;
 }
 cout << F << endl;
 return 0;
}

//lab 2, task 1.3 STILL IN WORK
#include <iostream>
using namespace std;
#include <math.h>
int main() {
  float N;
  float i;
  float A;
  cout << "Введите N " << endl;
  cin >> N;
  A = 1;
  for (i=1; i<=N; i++) {
   A = 1 + (1 / (i * i));
   cout << A << endl;
  }
  cout << A << endl;
  return 0;
}

//lab 2, task 1.4
#include <iostream>
using namespace std;
#include <math.h>
int main() {
  int N;
  int i;
  float A;
  cout << "Введите N " << endl;
  cin >> N;
  A = sqrt(2);
  cout << A << endl;
  for (i=1; i<=N; i++) {
   A = sqrt(2 + A);
   cout << A << endl;
  }
  cout << A << endl;
  return 0;
}

//lab 2, task 2
#include <iostream>
using namespace std;
int main() {
  float b, i, sum, SrAr; 
  cout << "Введите число, которое больше или равно 100" << endl;
  cin >> b;
  while (b < 100) {
    cout << "Введите число, которое больше или равно 100" << endl;
    cin >> b;
  }
  for (i=100; i<=b; i++) {
    sum += i*i;
  }
   SrAr = sum / (b - 100 + 1);
   cout << SrAr << endl;
  return 0;
}

//lab 2, task 3
#include <iostream>
using namespace std;
int main() {
  int i, j, N, x;
  x = 1;
  cout << "Введите число" << endl;
  cin >> N;
  for (i=1; i<=N; i++) {
    for (j=1; j<=N; j++) {
      x = j * i;
      if (j == N) {
        cout << x << endl;
      } 
       else cout << x << "   ";  
    }
  }
  return 0;
}
