with open("muscle.txt","r") as file:
    muscle = file.read().replace('\n','') #remove newlines

with open("brain.txt","r") as file:
    brain = file.read().replace('\n','') #remove newlines

if len(muscle)%2==1 and len(brain)%2==1:
    print("Ο πρώτος παίκτης χάνει")
else:
    print("Ο πρώτος παίκτης κερδίζει")
