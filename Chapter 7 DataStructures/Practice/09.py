# Concatenate: Given two lists, create a third list that alternates elements from the first and second.

list1 = [1, 2, 3, 4]
list2 = ['Ahmad', 'Ali', 'Hassan', 'Hussain']
combine = []
for c in zip(list1, list2):
    combine.append(c)
print(combine)