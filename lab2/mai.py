import csv

# данные для записи
data = [
    ["Имя", "Возраст", "Город"],  # Заголовки
    ["Алексей", 30, "Москва"],
    ["Мария", 25, "Санкт-Петербург"],
    ["Иван", 22, "Екатеринбург"]
]

# запись данных в CSV файл
with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data) # запись всех строк

# дозапись в файл
with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Ирина", 33, "Сочи"])