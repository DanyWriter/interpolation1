import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Text, Entry, Label, END

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

# Функция для построения графиков и отображения результатов
def plot_graphs():
    # Заданные узлы
    x_data = np.array([0, 0.5, 1, 1.5, 2])
    y_data = np.array([0, 1, 0, -1, 0])

    # Получение значения x от пользователя
    try:
        x_input = float(x_entry.get())
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Ошибка: Пожалуйста, введите корректное значение x.\n")
        return

    # Вычисление интерполяционного полинома Лагранжа
    y_interp = lagrange_interpolation(x_data, y_data, x_input)
    y_exact = np.sin(np.pi * x_input)  # Точное значение функции

    # Вывод результатов
    result_text.delete(1.0, END)  # Очистка предыдущих результатов
    result_text.insert(END, f"Значение интерполяционного полинома в x = {x_input}: {y_interp:.4f}\n")
    result_text.insert(END, f"Значение функции sin(π * x) в x = {x_input}: {y_exact:.4f}\n")
    result_text.insert(END, f"Разница: {y_interp - y_exact:.4f}\n")

    # Построение графиков
    x_fine = np.linspace(0, 2, 100)
    y_fine = np.sin(np.pi * x_fine)  # Точные значения функции
    y_interp_fine = [lagrange_interpolation(x_data, y_data, x) for x in x_fine]  # Значения интерполяции

    plt.figure(figsize=(10, 6))
    plt.plot(x_fine, y_fine, label='y = sin(πx)', color='blue')
    plt.plot(x_fine, y_interp_fine, label='Интерполяция Лагранжа', color='orange')
    plt.scatter(x_data, y_data, color='red', label='Узлы', zorder=5)
    plt.scatter(x_input, y_interp, color='green', label='Точка x', zorder=5)
    plt.title('Интерполяция Лагранжа и функция y = sin(πx)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

# Создание главного окна
root = Tk()
root.title("Интерполяция Лагранжа для y = sin(πx)")

# Создание метки и поля ввода для x
x_label = Label(root, text="Введите значение x:")
x_label.grid(row=0, column=0, padx=10, pady=10)

x_entry = Entry(root, width=20)
x_entry.grid(row=1, column=0, padx=10, pady=10)

# Создание кнопки для построения графиков
plot_button = Button(root, text="Построить графики и сравнить", command=plot_graphs)
plot_button.grid(row=2, column=0, padx=10, pady=10)

# Создание текстового поля для результатов
result_text = Text(root, width=60, height=10)
result_text.grid(row=3, column=0, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()