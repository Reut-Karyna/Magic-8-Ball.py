import random

name = "Callum"
question = "Will Callum sleep well tonight?"
answer = ""

random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definetely"
  print (answer)
elif random_number == 2:
  answer = "It is decidedly so"
  print (answer)
elif random_number == 3:
  answer ="Without a doubt" 
  print (answer) 
elif random_number == 4:
  answer = "Reply hazy, try again"
  print (answer)  
elif random_number == 5:
  answer = "Ask again later"
  print (answer)  
elif random_number == 6:
  answer = "Ask again later"
  print (answer)
elif random_number == 7:
  answer = "My sources say no"
  print (answer) 
elif random_number == 8:
  answer = "Outlook not so good"
  print (answer)
elif random_number == 9:
  answer = "Very doubtful"
  print (answer)
else:
  print("Error")     

print(name + " " + "asks:" + " " + question ) 
print ("magic 8-Ball's answer:" + answer)

