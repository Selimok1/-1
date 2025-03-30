n = int(input("Введите число n: "))
print("Все числа от 1 до n:")
for i in range(1, n + 1):
    print(i)
print("Квадраты чисел от 1 до n:")
for s in range(1, n + 1):
    print(s)
total_sum = sum(range(1, n + 1))
print(f"Сумма всех чисел от 1 до n: {total_sum}")
