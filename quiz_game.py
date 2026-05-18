# Python Practices
# Quiz Game
# This program asks questions and waits for user input. If the answer is correct, one point is added to the user's score and displayed at the end of the quiz

score = 0

question1 = input("What is 2 + 2? ")
if question1 == "4":
    print("That is correct!")
    score += 1 

question2 = input("What is the capital of England? ")
if question2 == "London":
    print("That is correct!")
    score += 1 

print("End Of Quiz!!")
print("Your score is:", score)
