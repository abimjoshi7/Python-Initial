comm=""
started=False
while True:
  comm=input(">").lower()
  if(comm=="start"):
    if started==True:
      print('Car already started')
    else:
      print("Car starts..")
      started=True
  if comm=='stop':
    if started==True:
      print("car is stopped")
      started=False
    else:
      print("car not started")
  if comm=="help":
    print('''
start-To start the car
stop-To stop the car
quit=To exit
''')
  if comm=='quit':
    break

