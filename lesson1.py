def mul_or_sum(first_number: int, second_number: int):
    mul = first_number * second_number

    return mul if mul <= 1000 else first_number + second_number


#############################################

def task2(number: int) -> int:
    result = 0
    for n in range(number + 1):
        if n <= number:
            result += n 
    return result
    

##############################################

# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))

# b = 34 
# c = 34
# a = mul_or_sum(b, c)

# print("Result ", a)

# user_number = int(input("Введите число: "))

# print ("Сумма чисел от 1 до ", user_number, " = ", task2(user_number))



def task3(numbers: list[int]) -> list[int]:
    result_numbers = []
    for n in numbers:
        if n > 150 and n <= 500:
            continue
        elif n > 500:
            break
        if n % 5 == 0:
            result_numbers.append(n)
    return result_numbers

# input_list = input("Введите список через пробел: ")
# strings_numbers = input_list.split(' ')
# numbers = []
# for n in strings_numbers:
#     numbers.append(int(n))

# print("Результат: ", task3(numbers))


def main():
    a = [4, 6, 12, 354, 56, 0]

    for num in a:
        print(task2(num))


if __name__ == "__main__":
    main()