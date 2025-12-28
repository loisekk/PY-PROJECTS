import random 
top_of_range = input("TYPE A NUMBER -> ") # it takes as str 

if top_of_range.isdigit(): # need to convert into this 
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("please choose number larger than '0' next time !:" )
        quit()
else:
    print("please type a number  next time !:" )
    quit()

random_number = random.randint(0 , top_of_range)
guesses = 0 

while True :
   guesses +=1
   user_guess = input("make a guess buddy !: ")
   if user_guess.isdigit(): 
    user_guess = int(user_guess)
   else:
    print("please type a number  next time !:" )
    continue
   
   if user_guess == random_number:
      print("YOU GOT IT BROO 😜")
      break
   elif user_guess > random_number:
         print("you were above the number ⬆️")
   else:
         print("you were below the number ⬇️")

print(f"YOU GOT it in {guesses} guesses pretty much hilirious 😵‍💫")