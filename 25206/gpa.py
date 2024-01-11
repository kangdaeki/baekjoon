d={ "A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0, "P":0.0, "N":0.0 }
gpa=0.0
total=0.0
for _ in range(20):
    subject,credit_str,grade=input().split()
    credit=float(credit_str)
    gpa+=credit*d[grade]
    if "P"!=grade and "N"!=grade:
        total+=credit
print(gpa/total)
