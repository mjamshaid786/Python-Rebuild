#Task 1 — Automated Server Reboot Countdown
#	Scenario: A system administrator needs a script that counts down #before a server goes down for maintenance.
#	Task: Write a while loop that prints a countdown from 10 down to #1. After the loop ends, print "Server is rebooting now!".


r = 10

while r >= 1:
    print(r)
    r -= 1
print("Server is rebooting now!")