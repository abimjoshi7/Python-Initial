i=0
while i==10:
  i+=1
  start=input("(type help for command list): ")
  if start=="help":
    print("start-To start the car \n stop-To stop the car \n quit-To exit")
  if start=="start":
    print("car is ready to go")
  elif start=="stop":
    print("car is stopped")
  elif start=="quit":
    break
  else:
    print("I don't understand")

