## Распаковка
my_list = [1, 2, 3, 4]
a, b, c, d = my_list
print(f'A: {a}, B: {b}, C: {c}, D: {d}')
print(type(my_list))
print(type(a))

text = 'Hello my beautiful world'
print(text)
text = text.split()
print(text)
text.append('!')
print(text)
text = ' '.join(text)
text = text[:24] + text[25:]
print(text)

