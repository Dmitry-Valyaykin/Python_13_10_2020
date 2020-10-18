"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
 Считаем 3 + 33 + 333 = 369
"""
namber = int(input('введите положитльное число: '))
if namber < 0:
    namber = False
    print('Ошибка, проверьте вводимое число')
act_1 = namber * namber
act_2 = act_1 * namber
act_3 = namber + act_1 + act_2
print(f'{act_3}')
