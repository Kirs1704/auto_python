# file_data = open('data.txt')
# print(file_data.read())
# file_data.close()


def read_file():
    with open('data.txt') as file_data:
        for line in file_data.readlines():
            yield line

s = read_file()
print(s)

def calc():
    x = int(input('Введи первое число: '))
    y = int(input('Введи второе число: '))
    try:
        result = x / y
        print(f'Результат: {int(result)}')
        return result
    except ZeroDivisionError:
        print('Ну ты чего? Делить на ноль нельзя!')
    except:
        print('Что-то пошло не так..')
calc()