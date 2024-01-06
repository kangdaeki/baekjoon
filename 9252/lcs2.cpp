#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
  string s1,s2;
  cin >> s1;
  cin >> s2;
  int m=s1.length();
  int n=s2.length();
  int** table=new int* [m+1];
  int** back=new int* [m+1];
  for (int i=0;i<=m;i++) 
  {
    table[i]=new int [n+1];
    back[i]=new int [n+1];
  }

  table[0][0]=0;
  back[0][0]=0;
  // 0: match, 1: right, -1: down
  for (int i=1;i<=m;i++)
  {
    table[i][0]=0;
    back[i][0]=-1;
  }
  for (int j=1;j<=n;j++)
  {
    table[0][j]=0;
    back[0][j]=1;
  }

  for (int i=1;i<=m;i++)
    for (int j=1;j<=n;j++)
      if (s1[i-1]==s2[j-1])
      {
        table[i][j]=1+table[i-1][j-1];
        back[i][j]=0;
      }
      else
      {
        if (table[i-1][j]>table[i][j-1])
        {
          table[i][j]=table[i-1][j];
          back[i][j]=-1;
        }
        else
        {
          table[i][j]=table[i][j-1];
          back[i][j]=1;
        }
      }
  cout << table[m][n] << "\n";
  if (0<table[m][n])
  {
    string lcs;
    int i=m;
    int j=n;
    while ((0<=i)&&(0<=j))
    {
      if ((0==i)&&(0==j)) break;
      switch (back[i][j])
      {
        case 0:
          lcs.append(1,s1[i-1]);
          i--;
          j--;
          break;
        case 1:
          j--;
          break;
        case -1:
          i--;
          break;
      }
    }
    reverse(lcs.begin(),lcs.end());
    cout << lcs << "\n";
  }

  for (int i=0;i<=m;i++)
    delete[] table[i];
  delete[] table;
}

