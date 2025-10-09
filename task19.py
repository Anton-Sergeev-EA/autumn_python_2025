#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm
# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv: 1) "C4.5"; 2) "k - means"

algoritm = [
    "C4.5",
    "k - means",
    "Метод опорных векторов",
    "Apriori",
    "EM",
    "PageRank",
    "AdaBoost",
    "kNN",
    "Наивный байесовский классификатор",
    "CART"
]

# Открываю файл для записи.
with open('algoritm.csv', 'w', encoding='utf-8') as file:
    # Перебираю элементы списка с нумерацией.
    for index, value in enumerate(algoritm, start=1):
        # Форматирую строку согласно требованиям.
        line = f"{index}) \"{value}\"\n"
        # Записываю в файл.
        file.write(line)

print("Файл algoritm.csv успешно создан")

