import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from tkinter import Tk, Button, Text, Entry, Label, END

# Функция для построения графиков и отображения результатов
def plot_graphs():
    # Получение узлов из текстового поля
    nodes_input = nodes_entry.get()
    try:
        # Преобразование введенных узлов в массив чисел
        x_data = np.array([float(x) for x in nodes_input.split(',')])
        y_data = np.log(1 + x_data**2)  # Вычисление y(x) = ln(1 + x^2)

        # Создание кубического сплайна
        cs = CubicSpline(x_data, y_data)

        # Создание более тонкой сетки для построения графиков
        x_fine = np.linspace(min(x_data), max(x_data), 100)
        y_fine = np.log(1 + x_fine**2)  # Точные значения
        y_spline = cs(x_fine)  # Значения сплайна

        # Построение графиков
        plt.figure(figsize=(10, 6))
        plt.plot(x_fine, y_fine, label='y(x) = ln(1 + x^2)', color='blue')
        plt.plot(x_fine, y_spline, label='Кубический сплайн', color='orange')
        plt.scatter(x_data, y_data, color='red', label='Узлы', zorder=5)
        plt.title('Интерполяция кубическими сплайнами')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.show()

        # Вывод результатов в текстовом поле
        result_text.delete(1.0, END)  # Очистка предыдущих результатов
        result_text.insert(END, "Интерполяция кубическими сплайнами выполнена.\n")
        result_text.insert(END, "График функции и сплайна построен.\n")

    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Ошибка: Пожалуйста, введите узлы в формате: x1,x2,x3,...\n")

# Создание главного окна
root = Tk()
root.title("Интерполяция кубическими сплайнами для y(x) = ln(1 + x^2)")

# Создание метки и поля ввода для узлов
nodes_label = Label(root, text="Введите узлы (через запятую):")
nodes_label.grid(row=0, column=0, padx=10, pady=10)

nodes_entry = Entry(root, width=50)
nodes_entry.grid(row=1, column=0, padx=10, pady=10)

# Создание кнопки для построения графиков
plot_button = Button(root, text="Построить графики", command=plot_graphs)
plot_button.grid(row=2, column=0, padx=10, pady=10)

# Создание текстового поля для результатов
result_text = Text(root, width=60, height=10)
result_text.grid(row=3, column=0, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()