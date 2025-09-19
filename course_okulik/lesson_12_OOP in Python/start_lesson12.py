import json

class Animal():
    def __init__(self, name):
        self.name = name
        print(f'Создано животное {self.name}')

    def speak(self):
        pass

    def go(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f'Эта собака породы {self.breed}')

    def speak(self):
        print('Собака лает')

    def go(self):
        print('Собака бежит')

my_dog = Dog('Джек', 'Дворняга')
my_dog.go()
my_dog.speak()


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f'Эта кошка породы {self.breed}')

    def speak(self):
        print(f'{self.name} мяукает')

    def go(self):
        print(f'{self.name} крадется')

some_cat = Cat('Мурка', 'Сиамская')
some_cat.go()
some_cat.speak()
print()

# file_data = open('data1.txt')
# data = json.loads(file_data.read())
# #data = json.loads(data)
# print(data['Country'])
# file_data.close()

def open_data_file(some_file):
    file_data = open(some_file)
    data = json.load(file_data)
    print(f'Содержимое файла: {data}')
    print(f'Страна: {data['Country']}')
    print(f'Температура: {data['avg_temp']}')
    print('=================================================')
    file_data.close()

open_data_file('data1.txt')
open_data_file('data2.txt')