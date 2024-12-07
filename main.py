import tkinter as tk
import subprocess
import os

def run_script(script_name):
    """Запускает указанный скрипт."""
    # Получаем полный путь к скрипту
    script_path = os.path.join(os.getcwd(), script_name)
    import sys
    subprocess.run([sys.executable, script_path])


# Создаем главное окно
root = tk.Tk()
root.title("Мой проект")

# Создаем кнопки для запуска скриптов
button1 = tk.Button(root, text="Запустить скрипт 1", command=lambda: run_script('target1.py'))
button1.pack(pady=10)

button2 = tk.Button(root, text="Запустить скрипт 2", command=lambda: run_script('target2.py'))
button2.pack(pady=10)

button3 = tk.Button(root, text="Запустить скрипт 3", command=lambda: run_script('target3.py'))
button3.pack(pady=10)

button3 = tk.Button(root, text="Запустить скрипт 4", command=lambda: run_script('target4.py'))
button3.pack(pady=10)

# Запускаем главный цикл
root.mainloop()