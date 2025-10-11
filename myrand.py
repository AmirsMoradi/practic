import random
winner_list=[]

def my_winner():
   while True:
      name = input("Enter your name: ")
      if name == "exit":
           break
      else:
       winner_list.append(name)

   x = random.choice(winner_list)
   print(winner_list)
   print(x)



my_winner()