def decorator(func):
    # код
    # код
    ...


@decorator
def censor(text):
    return f'текст {text} проверен'


print(censor('Hello'))
print(censor('Какая-то бяка'))


# текст Hello проверен
# Не пишите бяка!