list = ['1', 'name', '23', 'city']

# filter( function, value)
for c in filter (str.isalpha, list):
    print(c)
print("-" * 20)
list2 = ['23', '233']
for i in filter (str.isnumeric, list):
    print(i)