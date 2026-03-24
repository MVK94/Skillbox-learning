"""
Примеры ввода

path = 'C:/{user}/'.format()

path = 'C:/{user}/'.format(user = user_name)

path = 'C:/{0}/{1}'.format(user_name, file)

path = f"C:/{user_name}/"

"""


#5.2.1
"""
name = input('Имя: ')
number = input('Номер заказа: ')
path ='Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!'.format(
    name = name, 
    number = number
)
print(path)
"""

#5.3.1
"""import re
text_list = ["Пекс", "Питрик", "Горох","пукнул"]
counter = [0 for x in range(0, len(text_list))]
print(counter)
text = " Однажды утром Пекс и Питрик проснулись, и начали петь. Горох спал и пукнул и пукнул иии пукнул. "

words = re.findall(r"\w+", text)
print(words)

for word in words:
    if word in text_list:
        for j in text_list:
            if j == word:
                counter[text_list.index(word)] += 1

print(counter)"""

#5.3.2
"""text = input("Введите текст: ")

result = " ".join(text.split())

print("Исправленный текст:", result)"""

#5.4.2
user_name = input("Введите пользователя: ")
file_name = input("Введите имя файла: ")

path = 'C:/[{user}/docs/folder/{new_file}'.format(
    user = user_name,
    new_file = file_name
)

if not path.endswith('.txt'):
    print('Ошибка: неверное расширение файла. ')
elif not path.startswith('C:/'):
    print('Ошибка: неверно указан диск.')
else:
    print("Путь к файлу: ", path)

