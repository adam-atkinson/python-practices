# Python Practices
# Random Selector
# This program uses the random module to select a random name from the list and displays the result

import random 

team1 = ["Adam", "Amelia", "Reuben", "Gail", "Katie", "David"]
team2 = ["Jessie", "Billy", "Toby", "Hope", "Nathaniel", "Louise"]

captain1 = random.choice(team1)
captain2 = random.choice(team2)

print("Team 1 Captain is: ", captain1) 
print("Team 2 Captain is: ", captain2)
