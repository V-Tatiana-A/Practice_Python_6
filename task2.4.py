# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

from random import randint as rnd

print('1 ЭТАП')
length=int(input('Введите размер списка: '))
# for i in range (length):
#     array_1.append(rnd(1000,9999))
# Замена ниже:
array_1=[rnd(1000,9999) for i in range(length)]

print(array_1)

print('2 ЭТАП')
number=input('Введите цифру: ')
# for i in range(len(array_1)):
#     array_1[i]=str(array_1[i]).replace(number, '')
# Замена ниже:
array_1=[str(array_1[i]).replace(number, '') for i in range(len(array_1))]
print('[',end='')
print(*array_1, sep=', ', end='] \n')

print('3 ЭТАП')
def sum_of_digits (element):
    el=int(element)
    sum=0
    while el!=0:
        sum+=el%10
        el//=10
    if sum//10==0:
        return sum
    else:
        return sum_of_digits (sum)

# for i in range (len(array_1)):
#     result_array.append(sum_of_digits(array_1[i]))
# Замена ниже:
result_array=[sum_of_digits(array_1[i]) for i in range(len(array_1))]
print(result_array)

print('4 ЭТАП')
short_array=[]
for j in range (len(result_array)):
    if result_array[j] not in short_array:
        short_array.append(result_array[j])
print(short_array)






