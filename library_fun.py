# Библиотека функций

def fibonacci(N):           #Функция определения n чисел Фибоначчи
    if (N < 0):
        raise ValueError("Число не может быть отрицательным")
    elif (N == 0):
        return [0]
    fib = ([0, 1])
    for i in range(2, N):
        fib.append(fib[-1] + fib[-2])
    return fib

def bubble_sort(arr):               #Функция сортировки пузырьком
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def calculator(a, b, op):     #Функция калькулятора
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("На ноль делить нельзя!")
    else: raise ValueError ("Введите данные по примеру: def name(a, b, operation)")
