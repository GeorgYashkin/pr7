def integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")

print("Введите значения a, b, c для уравнения x = a - b - 4c:")
a = integer("Введите a: ")
b = integer("Введите b: ")
c = integer("Введите c: ")

result = a - b - 4 * c
print("x =", result)
