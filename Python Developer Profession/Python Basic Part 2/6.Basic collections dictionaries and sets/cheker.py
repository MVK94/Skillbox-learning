import os
import time

# Папка, где лежит скрипт
folder = os.path.dirname(os.path.abspath(__file__))

# Список файлов при старте
known_files = set(os.listdir(folder))

print("Отслеживание запущено...")
while True:
    time.sleep(1)  # проверка каждую секунду

    current_files = set(os.listdir(folder))

    # ищем новые файлы
    new_files = current_files - known_files

    if new_files:
        for file in new_files:
            print(f"Новый файл появился: {file}")

    known_files = current_files





