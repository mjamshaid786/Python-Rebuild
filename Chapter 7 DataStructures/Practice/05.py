marks = [45, 78, 90, 33, 88]

fail = any(m < 40 for m in marks)
print(fail)
pas = all(m >= 40 for m in marks)
print(pas)