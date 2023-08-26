a=0
b=0
c=0
for a in range(1, 10):
for b in range(1, 10):
for c in range(1, 10):
    if a*100+b*10+c==a*a*a+b*b*b+c*c*c:
        print(f"{a}{b}{c}")