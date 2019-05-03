# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


def get_sum(number):
    five = set(range(0, number, 3))
    three = set(range(0, number, 5))
    return five.union(three)


print(sum(get_sum(1000)))
