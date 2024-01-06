#include <iostream>
using namespace std;
int main()
{
  bool pos_data[1000001]={false};
  bool neg_data[1000001]={false};
  int N=0;
  cin >> N;
  for (int i=0;i<N;i++)
  {
    int n=0;
    cin >> n;
    if (n>=0) pos_data[n]=true;
    else neg_data[-n]=true;
  }
  for (int i=1000000;i>0;i--) if (neg_data[i]) cout << -i << "\n";
  for (int i=0;i<=1000000;i++) if (pos_data[i]) cout << i << "\n";
  return 0;
}
