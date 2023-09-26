"""Задача №31. 
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21"""
num=int(input('В ведите позицию для выведения числа фибоначи: '))

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-2)+fib(n-1)

list_1=[]
for i in range(1,num+1):
    list_1.append(fib(i))
print(list_1) # выдача списка последовательности фибоначи до числа n
print(fib(num)) # выдача позиции числа фибоначи