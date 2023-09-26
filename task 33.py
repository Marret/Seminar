"""Задача №33. 
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1"""

"""Решение студентов"""
import random

MIN_MARK=1
MAX_MARK=5
lst_2=[4, 1, 1, 2, 2] # выдаёт [4, 1, 1, 1, 1] ???
lst_3=[4,4,1, 1, 2, 2] #[1, 1, 1, 1, 2, 2] почему так?
# print(lst_1 := [random.randint(MIN_MARK,MAX_MARK) for i in range
                # (int(input('В ведите количество оценок в журнале: ')))] )



def find_values(array):
    min_vas=MAX_MARK
    max_vas=MIN_MARK
    for i in array:
        if i<min_vas:
             min_vas=i
        elif i>max_vas:
             max_vas =i
    
    for i in range(len(array)):
         if array[i] == max_vas:
              array[i]= min_vas
    return array
# print(find_values(lst_1))

print(find_values(lst_2))
print(find_values(lst_3))

"""Решение от Стоуна"""
import random

# MIN_MARK=1
# MAX_MARK=10
# print(lst_1 := [random.randint(MIN_MARK,MAX_MARK) for i in range(10)] )
# lst_2=[4, 1, 1, 2, 2]
# def change_mark(lst:lst_1):
#     maximum=max(lst) # присваиваем максимальное значение в списке через функцию max
#     minimum=min(lst) # присваиваем минимальное значение через функцию min
#     for i in range(len(lst)):
#           if lst[i] == maximum:
#                lst[i] = minimum
#     # return lst

# change_mark(lst_1)
# print(lst_1)
# change_mark(lst_2)
# print(lst_2)
          



