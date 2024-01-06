#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int A[5000001];
int N,K;

int partition(int l, int r, int K)
{
  int i,j,m;
  int tmp;
  int offset;

  if (l>=r) return l;
  srand((unsigned int)time(NULL));
  offset = l+rand()%(r-l+1);
  if (offset!=l) { tmp=A[l]; A[l]=A[offset]; A[offset]=tmp; }
  i=l+1;
  j=r;
  while (i<=j)
  {
    while ((i<=r)&&(A[i]<=A[l])) i++;
    while ((j>=l+1)&&(A[j]>=A[l])) j--;
    if (i<j) { tmp=A[i]; A[i]=A[j]; A[j]=tmp; }
  }
  if ((j<K)&&(K<i)) return K;
  m=j+(i-j)/2;
  tmp=A[l]; A[l]=A[m]; A[m]=tmp;
  return m;
}

int main()
{
  int i=0;
  int l,r;
  int index,index1,index2;

  scanf("%d",&N);
  scanf("%d",&K);
  for (i=0;i<N;i++) scanf("%d",&A[i]);
  K--;
  l=0;
  r=N-1;
  index1=partition(l,r,K);
  index2=partition(l,r,K);
  if (abs(K-index1)<abs(K-index2)) index=index1; else index=index2;
  while (index!=K)
  {
    if (index<K) l=index+1; 
    else if (index>K) r=index-1;
    else break;
    index1=partition(l,r,K);
    index2=partition(l,r,K);
    if (abs(K-index1)<abs(K-index2)) index=index1; else index=index2;
  }
  printf("%d\n",A[K]);
  return 0;
}
