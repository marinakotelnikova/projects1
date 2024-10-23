# Проект над виджетом банковских операций клиента.

## Создала модуль processing.py.
## Создала 2 функции:
## 1 - Функция принимает на вход список словарей с данными о банковских операциях и параметр state. возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.Параметр state функции имеет значение по умолчанию 'EXECUTED'.
       
## 2 - Функция принимает на вход список словарей и параметр порядка сортировки,возвращает новый список, в котором исходные словари отсортированы по дате.Параметр порядка сортировки функции имеет значение по умолчанию 'True'.

## В модулmь main.py методом import функции из модуля src/processing,py вывожу данные.

### Провела проверку через flake8, mypy.

### Сделали проверку через Pytests модули masks.py, widget.py, processing.py.
