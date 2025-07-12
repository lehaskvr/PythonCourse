a = [1, 2, 6, 7, 5, 3]

for idx, val in enumerate(a):
    print(idx, val)

l1 = ["Hello", "best"]
l2 = ["the", "World"]

for val1, val2 in zip(l1, l2):
    print(val1, val2)


a.sort()

print(a)

# print(a[::-1])
print(list(reversed(a)))

def add(a: int, b: int):
    return a + b

# lambda a, b: a + b # 1, 2 = 3
# lambda s: print("Hello, World!") # None

def is_odd(el: int):
    return el % 2 == 0

# print(list(filter(lambda el: el % 2 == 0, a)))
print(list(filter(is_odd, a)))

print(list(filter(lambda el: el % 2 == 0 or el - 1 == 0, a)))

a = [2.0, 2.1, 54.54, 8.21]

a.append(2.3)

print(a)

b = [2.2, 3.2, 3.1]
a.extend(b)

print(a)

a.insert(2, 5.23)
print(a)

a.pop()

a.append(2.0)

a.remove(2.0)

print(a)


# tuple

a = 2, 3, 5

def div_and_mod(a: float, dividor: int) -> tuple[int, float]:
    return int(a // dividor), float(a % dividor)

integer_part, float_part = div_and_mod(2.51, 2)
print(integer_part)
print(float_part)

a = div_and_mod(2.51, 2)
print(a)

a = [1, 5, 3, 3, 2, 2]
b = [1, 3, 5]

print(a > b)
max_value = max(a) # 5
min_value = min(a) # 1

print(a.count(3))


l1 = ["M", "na", "i", "Al"]
l2 = ["y", "me", "s", "ex"]

def sum_of_lists(list1: list, list2: list) -> list:
    result = []
    for l1, l2 in zip(list1, list2):
        result.append(l1 + l2)
    return result

print(sum_of_lists(l1, l2))

result1 = " "

print(result1.join(sum_of_lists(l1, l2)))


a = [1, 2, 5, 7, 8, 9]

def square_of_numbers(list1: list) -> list:
    list2 = []
    for n in list1:
        list2.append(n**2)
    return list2

print(square_of_numbers(a))



l1 = ["Hello", "take"]
l2 = ["Alex", "Dave"]

# ["Hello Alex", "Hello Dave", "take Alex", "take Dave"]


def new_list(l1: list, l2: list) -> list:
    list3 = []
    for n in l1:
        for n1 in l2:
            list3.append(f"{n} {n1}")
    return list3


print(new_list(l1, l2))