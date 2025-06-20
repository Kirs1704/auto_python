from faker import Faker

fake = Faker(locale='ru_RU')

# for _ in range(5):
#     print(fake.name())
#     print(fake.address())
#     print(fake.password())

data = fake.name().split()
surname, name, patron = data[0], data[1], data[2]
print(surname)
print(name)
print(patron)
