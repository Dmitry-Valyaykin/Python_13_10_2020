
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        break
    print('Ошибка введено не число')

result = int(user_num) + int(user_num * 2) + int(user_num * 3)
print(result)
print(int(user_num * 2))