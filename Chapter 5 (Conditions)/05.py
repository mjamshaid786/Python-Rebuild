# Task 5 — Student Grade & Performance Analytics
#	Scenario: An automated report card and feedback generator for teachers.
#	Input: Marks for 3 subjects (Math, Science, English) out of 100.
#	Logic: Calculate the average score.
#	Average >= 90: Grade A (Remark: Outstanding)
#	Average >= 75 and < 90: Grade B (Remark: Good Job)
#	Average >= 50 and < 75: Grade C (Remark: Needs Improvement)
#	Average < 50: Grade F (Remark: Failed)
#	Output: Print the Average Percentage, Assigned Grade, and Teacher's Remark.


# 1. Collect all inputs upfront
math = int(input("Enter obtained marks in Maths: "))
eng = int(input("Enter obtained marks in English: "))
science = int(input("Enter obtained marks in Science: "))

# 2. Validate all inputs at once (checking for > 100 or negative marks)
if math > 100 or eng > 100 or science > 100 or math < 0 or eng < 0 or science < 0:
    print("Error: Please enter valid marks between 0 and 100 for all subjects.")
else:
    # 3. Calculate average only if inputs are valid
    avg = (math + eng + science) / 3
    
    print(f"\nAverage Percentage: {avg:.2f}%")
    
    # 4. Run the grading system
    if avg >= 90:
        print("Grade: A\nTeacher Remarks: Outstanding")
    elif avg >= 75:  # No need for 'and avg < 90' because the 'if' above already caught anything 90 or higher
        print("Grade: B\nTeacher Remarks: Good Job")
    elif avg >= 50:
        print("Grade: C\nTeacher Remarks: Needs Improvement")
    else:
        print("Grade: F\nTeacher Remarks: Failed")