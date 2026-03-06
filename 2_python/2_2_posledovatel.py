import time
import tracemalloc

"""
Решение через математическую формулу.
Сумма чисел от 1 до n = n*(n+1)/2.
Вычитаем фактическую сумму списка — получаем пропущенное число.
Дополнительная память не используется вообще.
"""
def missing_number_v1(nums: list[int]) -> int:
    n = len(nums) + 1
    expected = n * (n + 1) // 2
    return expected - sum(nums)

"""
Решение через XOR.
x ^ x = 0, x ^ 0 = x — поэтому если XOR-им все числа
от 1 до n и все числа списка, все пары взаимно уничтожатся,
останется только пропущенное число.
Дополнительная память не используется.
"""
def missing_number_v2(nums: list[int]) -> int:
    n = len(nums) + 1
    xor_full = 0
    for i in range(1, n + 1):
        xor_full ^= i
    for num in nums:
        xor_full ^= num
    return xor_full


"""
Вспомогательная функция для замера
"""
def measure(func, nums: list[int], label: str):
    tracemalloc.start()
    start = time.perf_counter()

    result = func(nums)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"  [{label}]  Результат: {result}")
    print(f"           Время:     {(end - start) * 1_000_000:.3f} мкс")
    print(f"           Память:    {peak} байт (пик)\n")


examples = [
    ([1, 2, 3, 4, 5, 6, 8, 9, 10, 11],          7),
    ([2, 3, 4, 5, 6],                             1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13],   12),
]

for i, (nums, expected) in enumerate(examples, 1):
    print(f"Пример {i}: nums={nums}")
    print(f"          Ожидается: {expected}")
    measure(missing_number_v1, nums, "Решение 1 (формула суммы)")
    measure(missing_number_v2, nums, "Решение 2 (XOR)          ")

'''
Пример 1: nums=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
          Ожидается: 7
  [Решение 1 (формула суммы)]  Результат: 7
           Время:     485.400 мкс
           Память:    48 байт (пик)        

  [Решение 2 (XOR)          ]  Результат: 7
           Время:     159.000 мкс
           Память:    80 байт (пик)        

Пример 2: nums=[2, 3, 4, 5, 6]
          Ожидается: 1
  [Решение 1 (формула суммы)]  Результат: 1
           Время:     5.400 мкс
           Память:    48 байт (пик)

  [Решение 2 (XOR)          ]  Результат: 1
           Время:     7.900 мкс
           Память:    80 байт (пик)

Пример 3: nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
          Ожидается: 12
  [Решение 1 (формула суммы)]  Результат: 12
           Время:     4.700 мкс
           Память:    48 байт (пик)

  [Решение 2 (XOR)          ]  Результат: 12
           Время:     7.500 мкс
           Память:    80 байт (пик)

Вывод: решение 1 (формула суммы)  более оптимально по времени и памяти
'''