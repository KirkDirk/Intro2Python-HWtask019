# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
 
num_degree = int(input('Введите степень многочлена: '))
with open('D:\SASLearn\HW(python)\HWtask019\data.txt', 'w') as dataf:
    for i in range(num_degree):
        num_ratio = random.randint(0, 100)
        if num_ratio != 0 and i<(num_degree-1): dataf.write(str(num_ratio)+'x^'+str(num_degree-i)+ ' + ')
        if num_ratio != 0 and i==(num_degree-1): dataf.write(str(num_ratio)+' = 0')
    