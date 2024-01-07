import sys
input=sys.stdin.readline
N,K=map(int,input().split())
A=list(map(int,input().split()))

def select_K(l,r,k):
    global A
    if l<r: 
        pivot=partition(l,r)
        if pivot==k: return
        elif k<pivot: select_K(l,pivot-1,k)
        else: select_K(pivot+1,r,k)

def partition(l,r):
    global A
    if l+1==r:
        if A[l]>A[r]: A[l],A[r]=A[r],A[l]
        return r
    pivot=A[l]
    i=l+1
    j=r
    while i<=j:
        while pivot<A[j] and j>0: j-=1
        while pivot>A[i] and i<len(A)-1: i+=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
            i,j=i+1,j-1
    A[l]=A[j]
    A[j]=pivot
    return j

select_K(0,N-1,K-1)
print(A[K-1])
