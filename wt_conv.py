wt=float(input("Weight: "))
z=input("kg or lbs: ")
q="kg"
w="lbs"
if z==q:
  res=str(wt*2.205)
  print(res[0:5]+" lbs")
elif z==w:
  res=str(wt/2.205)
  print(res[0:5]+" kg")

