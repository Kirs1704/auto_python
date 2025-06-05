import random
import helper
from course_okulik.lesson_8.helper import assist

print(random.random())
print(random.randint(0,5)) # Правая граница включительна
print(random.randrange(0,5)) # Правая граница не включительна
print(random.randrange(0,10, 2)) # у randrange можно указать шаг

# Пример применения random.choice
users =  ['user1', 'user2', 'user3']
print(random.choice(users))

helper.assist()
print(helper.variable)

