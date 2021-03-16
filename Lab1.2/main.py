#!/usr/bin/python3
from openpyxl import load_workbook
#from matplotlib import pyplot
# При установке matplotlib возникла ошибка
#          assert tag in supported_tags, "would build wheel with unsupported tag {}".format(tag)
#       AssertionError: would build wheel with unsupported tag ('cp39', 'cp39', 'macosx_11_0_universal2')
# По этому pyplot используется как концепт :(

# Получаем данные из файла Excel
wb = load_workbook("data_analysis_lab.xlsx")['Data']


# Функция для возврата значений из столбцов
def getvalue(x): return x.value


# Создаем списки с данными столбцов
list_a, list_c, list_d = wb['A'][1:], wb['C'][1:], wb['D'][1:]

#D = activity

# Извлекаем значение столбцов и формируем список
values_a, values_c, values_d = list(map(getvalue, list_a)), list(map(getvalue, list_c)), list(map(getvalue, list_d))

print(list(values_a))

#pyplot.plot(values_a, values_c)
#pyplot.plot(values_a, values_d)
#pyplot.show()