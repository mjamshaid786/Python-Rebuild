#Task 7 — High-Score Target Matcher
#	Scenario: A basic gaming loop looking for a specific winning score.
#	Task: Run a loop exactly 5 times asking the user to guess a hidden score number. If they don't find it within 5 attempts, print "Game Over".


number = input("Enter a Hidden Number: ")

attempts = 5

while attempts > 0:
    guess = input("Guess the word: ")
    if guess == number:
        print("You Win !")
    attempts -= 1
    print(f"Attempts left {attempts}")

print("Game Over !")