"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""

def first_sec_arg(a, b, c):

    if a>=b>=c:
        return a + b
    elif b>=c>=a:
        return b + c
    else:
        return c + a
print(first_sec_arg(9, 1, 3))
