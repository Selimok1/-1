import random
numbers = [random.randint(1, 100) for _ in range(10)] # Создаём список из 10 случайных чисел
max_value = max(numbers)
min_value = min(numbers)
total_sum = sum(numbers)
numbers.sort() # Сортируем список по возрастанию
print(f"Список случайных чисел: {numbers}\n"
      f"Максимальное значение: {max_value}\n"
      f"Минимальное значение: {min_value}\n"
      f"Сумма всех элементов списка: {total_sum}\n"
      f"Отсортированный список: {numbers}")