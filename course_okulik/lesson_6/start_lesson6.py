# Распечатать все слова, в которых есть бука "о" и выбросить из текста, текст в конце рапечатать.

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'.split()
print(text)
text2 = []
for word in text:
    if 'o' in word:
        print(word)
    else:
        text2.append(word)
print(' '.join(text2))