
num = int(input("Введіть трьохзначне число: "))
sum = 0
for i in range(3):
    sum += num % 10
    num //= 10
print("Сума цифр числа становить", sum)