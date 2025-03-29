# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
# В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.

import pandas as pd  # This is a sample Python script.

df = pd.read_csv("freelancer_earnings_bd.csv")

df.info()
df.describe()

print(df)

df = pd.read_csv("dz.csv")

df.info()
print(df)
df.fillna(value=0, inplace=True)
print(df)

group = df.groupby("City")["Salary"].mean()
print(group)
