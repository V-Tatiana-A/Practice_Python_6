# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

array = input('Ведите числа через пробел: ').split()
my_list = list(map(int, array))
# result=0
# for i in range(len(my_list)):
#     if i%2!=0:
#         result+=my_list[i]
# замена ниже:

result=sum(list(my_list[i] for i in range(len(my_list)) if not i%2==0))
print(result)

