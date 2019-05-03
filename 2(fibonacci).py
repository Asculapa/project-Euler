# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
import numpy as np


def get_sum(limit):
    dyn_matrix = np.array([[0, 1], [1, 1]])
    stat_matrix = dyn_matrix
    result = 0
    while dyn_matrix[1][1] < limit:
        dyn_matrix = np.dot(dyn_matrix, stat_matrix)
        if dyn_matrix[1][1] % 2 == 0:
            result += dyn_matrix[1][1]
    return result


print(get_sum(50))

# get_sum(10) = 10
# get_sum(50) = 44
# get_sum(4*10**6) = 4613732
