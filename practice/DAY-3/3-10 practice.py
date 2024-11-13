s = '''
pk: 1
title: "Классы и объекты"
author: "Иван Иванов"
views: 14356
review: 12
'''.strip().replace('"','').splitlines()

s = [row.split(':') for row in s]
s = dict(s)


class Bookstore:
    ...

for key, value in s.items():
    setattr(Bookstore, key, value)


print(Bookstore.__dict__)
