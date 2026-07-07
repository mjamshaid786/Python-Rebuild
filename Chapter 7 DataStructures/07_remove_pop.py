list = [1, 7, 5, 9, 4]
# in remove we give value as argument
list.remove(4)
print(list)
# for pop() we give index number instead of value
deleted_item = list.pop(-2)
print("Deleted Item: ", deleted_item)
print(list)