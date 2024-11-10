def integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")

print("Введите десятичное число")
a = integer("Введите число: ")

print("В двоичном виде:", str(bin(a)[2:]))
print("В восьмиричном виде:", str(oct(a)[2:]))
