x_set=set()
y_set=set()
x,y=map(int,input().split())
x_set.add(x)
y_set.add(y)
x,y=map(int,input().split())
if x in x_set: x_set.remove(x)
else: x_set.add(x)
if y in y_set: y_set.remove(y)
else: y_set.add(y)
x,y=map(int,input().split())
if x in x_set: x_set.remove(x)
else: x_set.add(x)
if y in y_set: y_set.remove(y)
else: y_set.add(y)
for x in x_set: print(x,end=' ')
for y in y_set: print(y)
