from datetime import date

year=date.today()
a=str(year)
b=a[:4]
c=int(b)
age=input("what is your birth year?: ")
d=int(age)
res=c-d
print(res)

