"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
def data_user(name, surname, year_birth, from_city, mail, phon_number):
    print(f'name - {name}; surname - {surname}; year_birth - {year_birth}; from_city - {from_city}; mail - {mail}; phon_number - {phon_number}')
data_user(name='Ivan', surname='Ivanov', year_birth='33', from_city='Moscow', mail='i@com',phon_number='555555') 