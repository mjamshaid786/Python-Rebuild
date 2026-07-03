# Task 2 — Network Port Scanner Range
#	Scenario: You are writing a mini network diagnostic tool to #display active ports.
#	Task: Use a for loop with range() to print all even port numbers #between 1024 and 1050 inclusive.


for port in range (1024, 1050):
    if port %2 == 0:
        print(port)

print("-" * 30)
print("Scanning Done!")
print("-" * 30)