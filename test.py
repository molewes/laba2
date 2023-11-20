import pytest
from library_fun import fibonacci, bubble_sort, calculator

# Тесты для функции определения чисел Фибоначчи
def test_fibonacci():
    assert fibonacci(0) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]


# Тесты для функции сортировки пузырьком
def test_bubble_sort():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 5]) == [1, 1, 2, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort([-3, -5, -2, -1, -4]) == [-5, -4, -3, -2, -1]


# Тесты для функции калькулятора
def test_calculator():
    assert calculator(5, 2, '+') == 7
    assert calculator(8, 3, '-') == 5
    assert calculator(4, 2, '*') == 8
    assert calculator(10, 5, '/') == 2
    with pytest.raises(ValueError):
        calculator(6, 0, '/')  # Тест на обработку деления на ноль


# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__])
