num=9
guess_limit=3
guess_count=0
while guess_count<guess_limit:
  guess=int(input("Guess: "))
  guess_count +=1
  if(guess==num):
    print("Correct")
    break
  else:
    print("try again")
    
