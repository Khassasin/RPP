from random import randint


# метод с использованием стандартных функций
def with_default():
    # ввод с клавиатуры
    def user_input(arr_len):
        a = input().split()
        for i in range(arr_len):
            a[i] = int(a[i])
        return a

    # генерация массива
    def pc_input(arr_len, a):
        for i in range(arr_len):
            a[i] = randint(-10, 10)

    # сортировка
    def insertion_sort(a):
        for i in range(1, len(a)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    print("1 - ввод с клавиатуры")
    print("2 - автогенерация массива")
    input_mode = int(input())
    arr = [0]
    # выбор ввода
    if input_mode == 1:
        print("Введите размер массива")
        arr_size = int(input())
        arr = [0] * arr_size
        print("Введите массив")
        arr = user_input(arr_size)
    elif input_mode == 2:
        arr_size = randint(2, 10)
        arr = [0] * arr_size
        pc_input(arr_size, arr)
        # вывод неотсортированного массива
        print(arr)
    else:
        print("Неверное число")
    insertion_sort(arr)
    # вывод массива
    print(arr)

# метод без использования стандартных функций
def without_default():
    # ввод с клавиатуры
    def user_input(arr_len):
        a = input().split()
        i = 0
        while i < arr_len:
            a[i] = int(a[i])
            i += 1
        return a

    # генерация массива
    def pc_input(arr_len, a):
        i = 0
        while i < arr_len:
            a[i] = randint(-10, 10)
            i += 1

    # сортировка
    def insertion_sort(a, a_size):
        i = 1
        while i < a_size:
            key = a[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
            i += 1

    print("1 - ввод с клавиатуры")
    print("2 - автогенерация массива")
    input_mode = int(input())
    arr = [0]
    arr_size = 0
    # выбор ввода
    if input_mode == 1:
        print("Введите размер массива")
        arr_size = int(input())
        arr = [0] * arr_size
        print("Введите массив")
        arr = user_input(arr_size)
    elif input_mode == 2:
        arr_size = randint(2, 10)
        arr = [0] * arr_size
        pc_input(arr_size, arr)
        # вывод неотсортированного массива
        print(arr)
    else:
        print("Неверное число")
    insertion_sort(arr, arr_size)
    # вывод массива
    print(arr)


print("1 - использовать стандартные функции")
print("2 - не использовать стандартные функции")
method_type = int(input())
if method_type == 1:
    with_default()
elif method_type == 2:
    without_default()
else:
    print("Неверный ввод")
