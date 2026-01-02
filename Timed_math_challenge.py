import random 
import time

OPEARATORS = ["+" , "-" , "*"]
MIN_OPEARAND = 3
MAX_OPEARAND = 12
TOTAL_PROBLEMS = 10 


def generate_Problem():
    left = random.randint(MIN_OPEARAND , MAX_OPEARAND)
    right = random.randint(MIN_OPEARAND , MAX_OPEARAND)
    opeator = random.choice(OPEARATORS)

    expr =str(left) + " " + opeator+ " " + str(right)
    answer = eval(expr) 
    return expr , answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()



for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_Problem()

    while True :
     guess = input("Problem" + str(i + 1) + ": " + expr  + " = ")
     if guess == str(answer) :
        break
     wrong += 1

end_Time = time.time()
Total_Time = round(end_Time - start_time, 2)

print("---------------------")
print("Nice Work !😜 You Finished in" , Total_Time , "Seconds!")
  

