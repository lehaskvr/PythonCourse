a = 2
b = 3

c = a + b # + - * / // % **

print(c)


##################

int, float, str, bool, None

a: int = 3
b: float = 3.4
# b = "ssdjosdf"
c: str = "Hello, World!"
d: bool = True  | False

n = None

#################

# beer = input("Введи количество литров пива: ") # "4"
# beer_friend = input("Введи количество литров пива твоего друга: ")

beer = 4
beer_friend = 5

total_beer = int(beer) + int(beer_friend)

print("Ваше общее количество пива: ", total_beer)

# beer = int(input("Введи количество литров пива: ") )
# beer_friend = int(input("Введи количество литров пива твоего друга: "))


#################

if beer == 5 and beer_friend == 16:
    print("Нифига вы пьете")
    beer = 2
elif beer == 4 or beer_friend == 2:
    print("Ну норм")
else:
    print(beer)


##################

list, dict, set

list_example = [2, 4, 6, 8, 9]
first_element = list_example[0] # 2
first_element = list_example[3] # 8

# list_example = [2, "2", 2.4, True]

# for i in range(len(list_example)):
#     print(list_example[i])

list_of_odds = []

print("List printing: ")
for num in list_example:
    if num % 2 == 0:
        # list_of_odds.insert(0, num) # Добавляет в начало массива
        list_of_odds.append(num)

print(list_of_odds)

list_example = [2, 2, 3, 4, 5, 5, 7, 8]

set_example = set(list_example)
set_1 = {1, 2, 4, 5}
print(set_example)

dict_example = {
    "one": 1, 
    "two": 2, 
    "three": 3
    }

print(dict_example["one"])


#####################

def add(first_number: float, second_number: float) -> float:
    return first_number + second_number

def sub(first_number: float, second_number: float) -> float:
    return first_number - second_number

def mul(first_number: float, second_number: float) -> float:
    return first_number * second_number

def div(first_number: float, second_number: float) -> float:
    return first_number / second_number


first_number = float(input("Введите первое число: "))
operation = input("Введите операцию: ")
second_number = float(input("Введите второе число: "))

result = None

if operation == "+":
   result = add(first_number, second_number)
elif operation == "-":
    result = sub(first_number, second_number)
elif operation =="*":
    result = mul(first_number, second_number)
elif operation =="/":
    result = div(first_number, second_number)
else:
    result = "Неизвестная операция"

print("Твой результат: ", result)

for i in range(50):
    if i - 2 == 32:
        continue
    elif i + 2 == 45:
        break

    i += 2