started=False

while True:
  if started==False:
    comm=input("the car is ready to start...:")
    if comm=="stop":
      print("error")
      continue
  else:
    comm=input("the car is started...:")
    if comm=="start":
      print("error")
      continue
    
  if comm=="start":
    print("car starts...")
    started=True
  if comm=="stop":
    print("the car stops")
    started=False
  if comm=="exit":
    break;
  if comm=="help":
    print('''
start-to start the car
stop-to stop the car
exit-to exit the game
''')


    

  
