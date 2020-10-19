"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict.
"""
namber = int(input('Ведите число от 1 до 12:>>> '))
winter = {12:'декабрь', 1:'январь', 2:'февраль'}
sprint = {3:'март', 4:'апрель', 5:'май'}
summer = {6:'июнь', 7:'июль', 8:'август'}
autumn = {9:'сентябрь', 10:'октябрь', 11:'ноябрь'}

for i in winter.keys():
    if i == namber:
        print('зима')
for i in sprint.keys():
    if i == namber:
        print('весна')
for i in summer.keys():
    if i == namber:
        print('лето')
for i in autumn.keys():
    if i == namber:
        print('осень')

