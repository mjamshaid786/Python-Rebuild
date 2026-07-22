# **kwargs are used when multi type data is used in input..

def user(**kwargs):
    print(kwargs)
user(
    name = 'Ibrahim',
    city = 'Madinah',
    age = 25
)