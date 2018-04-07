import random
import string


adjectives = ["Chilly","Cold", "Cuddly","Dumb"]
nouns = ["Dogoos","People","Swords","Axe"]

print("Hello sir, please allow me in securing you a password!\n")
print("But first, would you like me to gather new nouns and adjectives from a file? Or use the ones I have")


adjective= random.choice(adjectives)

noun = random.choice(nouns)

number=random.randrange(0,100)

special_char=random.choice(string.punctuation)

password = adjective+noun+str(number)+special_char

print("Here is your ultra seceret password:%s" %password)
