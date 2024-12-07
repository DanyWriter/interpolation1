import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Text, END, Label, Entry


# Функция для вычисления интерполяционного полинома Лагранжа
def lagrange_interpolation(x_data, y_data, x):
    n = len(x_data)
    y = 0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        y += term
    return y


# Функция для вычисления точных значений
def calculate_exact_values(midpoints):
    return [np.log(1 + mp ** 2) for mp in midpoints]


# Функция для построения графиков и отображения результатов
def plot_graphs():
    # Получение узлов от пользователя
    user_input = nodes_entry.get()
    try:
        x_data = np.array([float(x) for x in user_input.split(',')])
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Ошибка: введите корректные числовые значения узлов через запятую.")
        return

    y_data = np.log(1 + x_data ** 2)  # Вычисление y(x) = ln(1 + x^2)

    # Вычисление средних точек
    midpoints = [(x_data[i] + x_data[i + 1]) / 2 for i in range(len(x_data) - 1)]

    # Вычисление точных значений и значений интерполяции в средних точках
    exact_values = calculate_exact_values(midpoints)
    interpolated_values = [lagrange_interpolation(x_data, y_data, mp) for mp in midpoints]

    # Отображение результатов в текстовом поле
    result_text.delete(1.0, END)  # Очистка предыдущих результатов
    result_text.insert(END, "Средняя точка\tТочное значение\tИнтерполированное значение\n")
    result_text.insert(END, "-----------------------------------------\n")
    for mp, exact, interp in zip(midpoints, exact_values, interpolated_values):
        result_text.insert(END, f"{mp:.4f}\t{exact:.4f}\t{interp:.4f}\n")

    # Создание подграфиков
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    # Построение y(x) и интерполяционного полинома
    x_fine = np.linspace(min(x_data), max(x_data), 100)
    y_fine = np.log(1 + x_fine ** 2)
    y_interp_fine = [lagrange_interpolation(x_data, y_data, x) for x in x_fine]

    axs[0].plot(x_fine, y_fine, label='y(x) = ln(1 + x^2)', color='blue')
    axs[0].plot(x_fine, y_interp_fine, label='Интерполяция Лагранжа', color='orange')
    axs[0].scatter(x_data, y_data, color='red', label='Узлы')
    axs[0].set_title('Функция и интерполяция Лагранжа')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].legend()
    axs[0].grid()

    # Построение точных и интерполированных значений в средних точках
    axs[1].plot(midpoints, exact_values, label='Точные значения', marker='o', color='blue')
    axs[1].plot(midpoints, interpolated_values, label='Интерполированные значения', marker='x', color='orange')
    axs[1].set_title('Точные и интерполированные значения в средних точках')
    axs[1].set_xlabel('Средние точки')
    axs[1].set_ylabel('y')
    axs[1].legend()
    axs[1].grid()

    plt.tight_layout()
    plt.show()


# Создание главного окна
root = Tk()
root.title("Интерполяция Лагранжа для y(x) = ln(1 + x^2)")

# Создание метки и текстового поля для ввода узлов
nodes_label = Label(root, text="Введите узлы ( через запятую):")
nodes_label.grid(row=0, column=0, padx=10, pady=5)

nodes_entry = Entry(root, width=50)
nodes_entry.grid(row=1, column=0, padx=10, pady=5)

# Создание кнопки для построения графиков
plot_button = Button(root, text="Построить графики и показать результаты", command=plot_graphs)
plot_button.grid(row=2, column=0, padx=10, pady=10)

# Создание текстового поля для результатов
result_text = Text(root, width=60, height=15)
result_text.grid(row=3, column=0, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()