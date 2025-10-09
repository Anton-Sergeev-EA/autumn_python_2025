#todo: Дан массив размера N. Найти минимальное расcтояние между одинаковыми
# значениями в массиве и вывести их индексы. # Одинаковых значение может быть
# два и более!
# Пример: mass = [1,2,17,54,30,89,2,1,6,2]

def find_min_distances(arr):
    index_map = {} # Словарь для хранения индексов элементов.
    # Заполняю словарь индексами.
    for index, value in enumerate(arr):
        if value not in index_map:
            index_map[value] = []
        index_map[value].append(index)
    
    results = {} # Ищу минимальные расстояния.
    for value, indices in index_map.items():
        if len(indices) < 2:
            results[value] = None  # Нет пар для сравнения.
            continue
        
        min_distance = float('inf')
        min_pair = (0, 0)
        
        # Ищу минимальное расстояние между соседними индексами.
        for i in range(1, len(indices)):
            distance = indices[i] - indices[i - 1]
            if distance < min_distance:
                min_distance = distance
                min_pair = (indices[i - 1], indices[i])
        
        results[value] = min_pair
    
    return results

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
result = find_min_distances(mass)

for value, pair in result.items():
    if pair:
        print(
            f"Для числа {value} минимальное расстояние в массиве по индексам: "
            f"{pair[0]} и {pair[1]}")
    else:
        print(
            f"Для числа {value} нет минимального расстояния, т.к. элемент в "
            f"массиве один")

# Для числа 1 минимальное расcтояние в массиве по индексам: 0 и 7.
# Для числа 2 минимальное расcтояние в массиве по индексам: 6 и 9.
# Для числа 17 нет минимального расcтояния т.к элемент в массиве один.