from faker import Faker

fake = Faker()

# Idade maxima de 22 anos
print(fake.date_of_birth(maximum_age=22))
# 2020-03-04

# Idade minima de 22 anos
print(fake.date_of_birth(minimum_age=22))
# 1967-02-18
