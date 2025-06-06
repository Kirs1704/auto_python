import  datetime

products = [("Молоко", 80), ("Хлеб", 50), ("Сыр", 300), ("Масло", 150)]
sorted_products = sorted(products, key=lambda item: item[1])
print(sorted_products)
products.sort()
print(products)

print('=========================================')

my_list = [1, 2, 3, 4, 5]
new_list1 = []

#def multipy_x2(x):
#   return x * 2
#new_list1 = map(multipy_x2, my_list)

new_list1 = map(lambda x: x*2, my_list)
print(list(new_list1))
new_list2 = filter(lambda x: x % 2 == 0, my_list)
print(list(new_list2))

now_datetime = datetime.datetime.now()
print(now_datetime)