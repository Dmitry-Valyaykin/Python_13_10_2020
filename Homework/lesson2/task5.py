"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
  Если в рейтинге существуют элементы с одинаковыми значениями,
   то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

"""
namber = int(input('введите цифру:>>> '))
#namber = list(namber)
my_list = [7, 5, 3, 3, 2]
my_list.append(namber)
#my_list.sort(key=lambda row: row[0] reverse=True)
#sorted(my_list, key=lambda: reverse=True)
my_list.sort()
print(my_list)