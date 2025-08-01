def is_valid_email(email_string: str) -> bool:
    # Эта функция проверяет email. Ей не нужно знать ни про какой
    # конкретный генератор (self), ни про сам класс (cls).
    # Она работает только со своими входными данными.
    return "@" in email_string and "." in email_string.split('@')[1]

print(is_valid_email('test@mail.com'))

s='test@mail.com'.split('@')
print(s)
print(s[1])