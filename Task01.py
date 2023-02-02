# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трёхзначное число: '))
digit3 = (num % 10)
print(digit3)
digit2 = int((num/10)%10)
print(digit2)
digit1 = int(num / 100)
print(digit1)
sum = digit1 + digit2 + digit3
print(f'Сумма цифр числа {num} --> {sum}')