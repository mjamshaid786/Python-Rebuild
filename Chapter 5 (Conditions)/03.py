# Task 3 — Cyber Log: Failed Login Brute-Force Detector
#	Scenario: A security script analyzing server logs for potential brute-force attacks.
#	Input: A string representing a sequence of login attempts (e.g., "S,S,F,F,S,F,F,F,S", where 'S' is Success and 'F' is Failure).
#	Logic: Parse the string and check if there are 3 or more consecutive 'F' (Failures) anywhere in the log sequence.
#	Output: If 3 consecutive failures are found, print "ALERT: Suspicious Activity Detected! Account Locked." Otherwise, print "Log Status: Safe".

attempts = "S,S,F,F,S,F,F,F,S"

if "F,F,F" in attempts:
    print("ALERT: Suspicious Activity Detected! Account Locked")
else:
    print("Log Status: Safe")
