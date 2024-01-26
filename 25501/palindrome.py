T=int(input())
for _ in range(T):
    S=input()
    if S==S[::-1]: 
        print(1,len(S)//2+1)
    else: 
        print(0,end=' ')
        for i in range(len(S)):
            if S[i]!=S[len(S)-i-1]:
                print(i+1)
                break


