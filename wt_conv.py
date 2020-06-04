wt=float(input("Weight: "))
z=input("(K)g or (l)bs: ")
if z.upper()=="K":
  res=str(wt*2.205)
  print(f"It is {res[0:5]} lbs")
else:
  res=str(wt/2.205)
  print(f"It is {res[0:5]} kg")

