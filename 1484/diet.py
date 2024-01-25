import sys
G=int(sys.stdin.readline())
old,new=1,2
printed=False
while True:
    gap=new*new-old*old
    if gap>G and 1==new-old: break
    if gap==G:
        print(new)
        printed=True
        new+=1
    elif gap<G: new+=1
    else: old+=1
if not printed: print(-1)
