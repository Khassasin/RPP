import numpy as np


# ввод размеров матрицы
print("Введите количество строк и столбцов через пробел")
n, m = [int(i) for i in input().split()]
# открытие файла вывода
file = open("output.txt", "w")
file.write("Количество строк и столбцов " + str(n) + " " + str(m) + "\n")
# генерация матрицы
arr = np.random.randint(-10, 10, (n, m))
file.write(str(arr) + "\n")
# ввод номеров строки и столбца
print("Введите номер строки и столбца, которые будут разделять матрицу через пробел")
l, k = [int(i) for i in input().split()]
file.write("Номер строки и столбца, которые будут разделять матрицу " + str(l) + " " + str(k) + "\n")
# разделение матрицы
arr_left_top = arr[:l, :k]
arr_right_top = arr[:l, k:]
arr_left_bottom = arr[l:, k]
arr_right_bottom = arr[l:, k:]
# вывод результатов
file.write("Сумма верхней левой матрицы " + str(np.sum(arr_left_top)) + "\n")
file.write("Сумма верхней правой матрицы " + str(np.sum(arr_right_top)) + "\n")
file.write("Сумма нижней левой матрицы " + str(np.sum(arr_left_bottom)) + "\n")
file.write("Сумма нижней правой матрицы" + str(np.sum(arr_right_bottom)) + "\n")
file.close()
