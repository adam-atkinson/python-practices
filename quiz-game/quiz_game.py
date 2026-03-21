score = 0

answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1

print("Your score:", score)
