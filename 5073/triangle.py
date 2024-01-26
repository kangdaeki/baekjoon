while True:
    a,b,c=map(int,input().split())
    if 0==a and 0==b and 0==c: exit()
    if a==b==c:
        print("Equilateral")
        continue
    if a>=b+c or b>=a+c or c>=a+b:
        print("Invalid")
        continue
    if a==b or a==c or b==c:
        print("Isosceles")
        continue
    print("Scalene")
