import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, W, E
from tkinter import ttk

# Функция для вычисления полинома Лагранжа
def lagrange_interpolation(x_data, y_data, x):
    """
    Вычисляет полином интерполяции Лагранжа для заданных точек данных.

    Аргументы:
        x_data (list): Список x-координат точек данных.
        y_data (list): Список y-координат точек данных.
        x (float): Значение x, в котором нужно оценить полином.

    Возвращает:
        float: Интерполированное значение y при x.
    """
    n = len(x_data)
    y = 0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        y += term
    return y

# Функция для обработки нажатия кнопки
def calculate_interpolation():
    try:
        # Получение данных из полей ввода
        x_data_str = x_data_entry.get().split(",")
        y_data_str = y_data_entry.get().split(",")
        x_data = [float(x) for x in x_data_str]
        y_data = [float(y) for y in y_data_str]
        x_interp = float(x_interp_entry.get())

        # Вычисление интерполяции
        y_interp = lagrange_interpolation(x_data, y_data, x_interp)

        # Отображение результата
        result_label.config(text=f"Интерполированное значение при x = {x_interp}: {y_interp}")

        # Построение графика данных и интерполяции
        plt.figure()
        plt.plot(x_data, y_data, 'o-', label='Точки данных')
        x_values = np.linspace(min(x_data), max(x_data), 100)
        y_values = [lagrange_interpolation(x_data, y_data, x) for x in x_values]
        plt.plot(x_values, y_values, label='Полином Лагранжа', color='orange')
        plt.scatter(x_interp, y_interp, color='red', label='Интерполированная точка')
        plt.title('Интерполяция Лагранжа')
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректные числа.")

# Создание главного окна
root = Tk()
root.title("Калькулятор интерполяции Лагранжа")

# Создание полей ввода
x_data_label = Label(root, text="Введите точки данных x (через запятую):")
x_data_label.grid(row=0, column=0, sticky=W)
x_data_entry = Entry(root, width=50)
x_data_entry.grid(row=0, column=1)

y_data_label = Label(root, text="Введите точки данных y (через запятую):")
y_data_label.grid(row=1, column=0, sticky=W)
y_data_entry = Entry(root, width=50)
y_data_entry.grid(row=1, column=1)

x_interp_label = Label(root, text="Введите значение x для интерполяции:")
x_interp_label.grid(row=2, column=0, sticky=W)
x_interp_entry = Entry(root, width=50)
x_interp_entry.grid(row=2, column=1)

# Создание кнопки для вычисления
calculate_button = Button(root, text="Вычислить", command=calculate_interpolation)
calculate_button.grid(row=3, column=0, columnspan=2)

# Создание метки для результата
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Запуск приложения
root.mainloop()