#def my_func():
 #   print('Hello!')

# my_func()
# print('=======================================================')
#
# def my_decor_func(any_func):
#     print('Something before any func!')
#     any_func()
#     print('Something after any func!')
#
# my_decor_func(my_func)

print('=======================================================')

def my_decor_func2(any_func):
    def wrapper():
     print('Something before any func!')
     any_func()
     print('Something after any func!')
    return wrapper

#my_func = my_decor_func2(my_func)
@my_decor_func2
def my_func():
    print('Hello!')
my_func()
print('any code.....')
print('and more code.....')
print('and more.....')
@my_decor_func2
def my_func2():
    print('Hello again!')

print(my_func2)
my_func2()

print('=====================================================')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print('Способ с лямбда-функцией: ')
new_list2 = map(lambda x: x * 2, my_list)
print(list(new_list2))

print('Способ со списочными выражениями: ')
new_list = [x*2 for x in my_list]
print(new_list)

new_list3 = filter(lambda x: x % 2 == 0,  my_list)
print(list(new_list3))


some_list = [('one', 'two'), ('three', 'for')]
# Есть список с парами в виде кортежей, нужно разложить его на словарь

print('Вариант № 1: ')
some_dict = {}
for key, value in some_list:
    some_dict[key] = value
print(some_dict)

print('Вариант № 2: ')
some_dict2 = {key: value for key, value in some_list}
print(some_dict2)

print('Вариант № 3 (самый простой): ')
some_dict3 = dict(some_list)
print(some_dict3)


