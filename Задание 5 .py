import random
numbers = [random.randint(1, 100) for _ in range(20)] # Генерируем список из 20 случайных чисел от 1 до 100
even_numbers = [num for num in numbers if num % 2 == 0] # Все чётные числа из списка
divisibleby3 = [num for num in numbers if num % 3 == 0] # Все числа, которые делятся на 3
average = sum(numbers) / len(numbers) # Среднее арифметическое всех чисел в списке
print(f"Список случайных чисел: {numbers}\n"
      f"Чётные числа из списка: {even_numbers}\n"
      f"Числа, которые делятся на 3: {divisibleby3}\n"
      f"Среднее арифметическое всех чисел: {average:.2f}")