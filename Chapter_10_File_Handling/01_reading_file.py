#===========================================
#             FILE HANDILING
#===========================================

file = open("file.txt", "r")
data = file.read().strip()
print(data)
print(type(data))