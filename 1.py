# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


def get_set(number):
    five = set(range(0, number, 3))
    three = set(range(0, number, 5))
    return five.union(three)


print(sum(get_set(1000)))

# get_sum(10) = 23
# get_sum(1000) = 233168
