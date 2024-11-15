# __add__, __sub__, __mul__

# Домовая книга, загс, регистрация граждан


class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex.upper()
        self.status = None

    def __repr__(self):
        return f'{self.name} '


    def __add__(self, human):
        if isinstance(human,Human):
            if not self.status and self.sex != human.sex:
                self.status = human
                human.status = self
            else:
                raise TypeError("Человек уже в браке. Однополые браки запрещены")
        else:
            raise TypeError("Объект не человек")


    def __mul__(self, partner):
        if self.status == partner:
            return Human("Ваня", 'м')
        else:
            raise Exception("Вы не в браке. Детей делать нельзя")

    def __sub__(self, other):
        if self.status == other:
            self.status = None
            other.status = None


ivan = Human('Иван', 'm')
anna = Human('Анна', 'w')
elena = Human('Елена', 'w')


ivan + anna
user = ivan * anna

print(ivan, ivan.status)
print(anna, anna.status)

print(user)

ivan - anna

print(ivan, ivan.status)
print(anna, anna.status)