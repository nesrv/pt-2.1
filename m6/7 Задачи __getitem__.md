
## Задача 1 Объявите класс `Record (запись)`, который описывает одну произвольную запись из БД. 

Объекты этого класса создаются командой:

> r = Record(field_name1=value1,... , field_nameN=valueN)

где:

`field_nameX` - наименование поля БД; 
`valueX` - значение поля из БД.

В каждом объекте класса `Record` должны автоматически создаваться локальные публичные атрибуты по именам полей `(field_name1,... , field_nameN)` с соответствующими значениями. 

Например:

```python
r = Record(pk=1, title='Python-2', author='Серов')
```

В объекте r появляются атрибуты:

```python
r.pk # 1
r.title # Python-2
r.author # Серов
```
Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:

```python
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Серов' # доступ к полю author
print(r[1]) # Супер курс по ООП
```


> P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.

## Задача 2

необходимо для навигатора реализовать определение маршрутов. Для этого в программе нужно объявить класс `Track`, объекты которого создаются командой:

```python
tr = Track(start_x, start_y)

# где start_x, start_y - координата начала пути.
```
В этом классе должен быть реализован следующий метод:
```python
add_point(x, y, speed) 

# добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed.
```
Также с объектами класса Track должны выполняться команды:

```python
coord, speed = tr[indx] 

# получение координаты (кортеж с двумя числами) и скорости (число) для линейного сегмента маршрута с индексом indx
```
```python

tr[indx] = speed

# изменение средней скорости линейного участка маршрута по индексу `indx`
```
Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - число линейных сегментов в маршруте), то генерируется исключение командой:

```python
raise IndexError('некорректный индекс')
```
Пример использования класса :
```python
class Track:

    def __init__(self, start_x, start_y):
        

    def add_point(self, x, y, speed):
      

    def __getitem__(self, item):
        if ... :
            raise IndexError('некорректный индекс')
        return ...

    def __setitem__(self, key, value):
        if ... :
            raise IndexError('некорректный индекс')
         ...



tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError

```