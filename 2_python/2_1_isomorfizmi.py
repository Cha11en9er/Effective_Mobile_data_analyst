'''
Реализовать функцию (или тело функции), которая проверяет на изоморфность два слова. Пояснение: строки s и t называются изоморфными, если все вхождения каждого символа строки s можно последовательно заменить другим символом и получить строку t. Порядок символов при этом должен сохраняться, а замена — быть уникальной. Так, два разных символа строки s нельзя заменить одним и тем же символом из строки t, а вот одинаковые символы в строке s должны заменяться одним и тем же символом.
# Пример:
s = 'paper' 
t = 'title' 
print(is_isomorphic(s, t))
# Вывод: 
True
Оценить оптимальность решения по времени и памяти и прикрепить текст кода.
'''

import time
import tracemalloc

"""
Решение через два словаря.
Храним маппинг символов s -> t и обратный t -> s.
Если встречаем противоречие — строки не изоморфны.
"""
def is_isomorphic_v1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            if ct in t_to_s:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs

    return True

"""
Решение через паттерн первых вхождений.
Для каждого символа сохраняем позицию его первого появления.
Если паттерны позиций совпадают — строки изоморфны.
"""
def is_isomorphic_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    def encode(word: str) -> list:
        first_seen = {}
        pattern = []
        for i, ch in enumerate(word):
            if ch not in first_seen:
                first_seen[ch] = i
            pattern.append(first_seen[ch])
        return pattern

    return encode(s) == encode(t)


"""
Вспомогательная функция для замера времени и памяти
"""
def measure(func, s: str, t: str, label: str):
    tracemalloc.start()
    start = time.perf_counter()

    result = func(s, t)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"  [{label}]  Результат: {result}")
    print(f"           Время:     {(end - start) * 1_000_000:.3f} мкс")
    print(f"           Память:    {peak} байт (пик)\n")


examples = [
    ("paper",  "title",  True),
    ("foo",    "bar",    False),
    ("badc",   "baba",   False),
]

for i, (s, t, expected) in enumerate(examples, 1):
    print(f"Пример {i}: s={s!r}, t={t!r}  (ожидается: {expected})")
    measure(is_isomorphic_v1, s, t, "Решение 1 (двойной словарь)  ")
    measure(is_isomorphic_v2, s, t, "Решение 2 (индексы вхождений)")



'''
Пример 1: s='paper', t='title'  (ожидается: True)
  [Решение 1 (двойной словарь)  ]  Результат: True
           Время:     23.400 мкс
           Память:    280 байт (пик)

  [Решение 2 (индексы вхождений)]  Результат: True
           Время:     20.600 мкс
           Память:    408 байт (пик)

Пример 2: s='foo', t='bar'  (ожидается: False)
  [Решение 1 (двойной словарь)  ]  Результат: False
           Время:     7.400 мкс
           Память:    160 байт (пик)

  [Решение 2 (индексы вхождений)]  Результат: False
           Время:     10.600 мкс
           Память:    344 байт (пик)

Пример 3: s='badc', t='baba'  (ожидается: False)
  [Решение 1 (двойной словарь)  ]  Результат: False
           Время:     8.000 мкс
           Память:    160 байт (пик)

  [Решение 2 (индексы вхождений)]  Результат: False
           Время:     12.600 мкс
           Память:    344 байт (пик)

Вывод: решение 1 (двойной словарь)  более оптимально по времени и памяти
'''