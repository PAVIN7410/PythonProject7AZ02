# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
#
# ​
#
# # Параметры нормального распределения
#
# mean = 0 # Среднее значение
#
# std_dev = 1 # Стандартное отклонение
#
# num_samples = 1000 # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
#
# data = np.random.normal(mean, std_dev, num_samples)
#
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​
#
# import numpy as np
#
# random_array = np.random.rand(5) # массив из 5 случайных чисел
#
# print(random_array)
#
# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны​

import pandas as pd
import random

import numpy as np
import matplotlib.pyplot as plt

#Генерируем 1000 случайных данных из нормального распределения
mean = 0  # среднее
std_dev = 1  # стандартное отклонение
data = np.random.normal(mean, std_dev, 1000)

# Создаем гистограмму
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма случайных данных из нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()



a = np.random.rand(5) # массив из 5 случайных чисел
b = np.random.rand(5) # массив из 9 случайных чисел
print(a, b)
plt.scatter(a, b)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('График рассеяния')
plt.show()