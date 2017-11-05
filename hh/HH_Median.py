print "Вычисление медианы двух массивов\n"

# Ввод данных
a1 = raw_input('Введите числа первого массива:')
a2 = raw_input('Введите числа второго массива:')
a3 = a1 + ' ' + a2

# Поиск чисел в строке и добавление их в массив
a3 = a3.split()

# Перевод строковых значений в чисельные
a4 = []
for val in a3:
    try:
        val=int(val)
        a4.append(val)
    except:
        val=float(val)
        a4.append(val)
        
a4.sort()

# Вычисление медианы
def median(x):
    lenmid = len(x)/2
    if len(x)%2==0:
        return (int(x[lenmid-1])+int(x[lenmid]))/2.0
    return int(x[lenmid])

# Вывод результата, вызов функции
print "\nМедиана равна ", median(a4)
