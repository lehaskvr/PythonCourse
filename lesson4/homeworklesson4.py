def creating_a_string(first_string:str, second_string:str) -> str:
    result_string = []
    second_string = second_string[::-1]
    if len(first_string) - len(second_string) > 0:
        n = first_string[-(len(first_string) - len(second_string))::1]
        for first_string, second_string in zip(first_string, second_string):
            result_string.append(first_string + second_string)
        result_string.append(n)
    elif len(first_string) - len(second_string) < 0:
        n = second_string[(len(first_string) - len(second_string))::1]
        for first_string, second_string in zip(first_string, second_string):
            result_string.append(first_string + second_string)
        result_string.append(n)
    else:
        for first_string, second_string in zip(first_string, second_string):
            result_string.append(first_string + second_string)
    result_string = "".join(result_string)
    return result_string

def sort_list_of_int(test_list:list[int], condition:bool) -> list[int]:
    for n in range(len(test_list)):
        for a in range(len(test_list) - n - 1):
            if test_list[a] > test_list[a + 1]:
                test_list[a], test_list[a + 1] = test_list[a + 1], test_list[a]
    if condition == True:
        return test_list
    else:
        return test_list[::-1]

def average_in_string(s1:str) -> int:
    list1 = []
    b = 0
    c = 0
    for n in s1:
        list1.append(n)
    for n in range(len(list1)):
        if list1[n] != int:
            continue
        else:
            list1[n] = int(list1[n])
            b += list1[n]
            c += 1
    if b == 0:
        print("Цифры не найдены")
    else:
        average = b / c
        print("Сумма цифр:", b, "Среднее арифмитическое:", average)

def cheking_for_prime_numbers(number1:int):
    for n in range(2, number1):
        number1 % n
    if number1 % n != 0:
        print("Число простое")
    else:
        print("Число не простое")


def main():
    test_string1 = "hello"
    test_string2 = "world"
    first_string = "пока"
    second_string = "привет"
    test_list1 = [5, 2, 9, 1, 5, 6]
    condition1 = False
    condition2 = True
    string1 = "abc123def"
    string2 = "hello"
    test_number = 5
    test_number1 = 4
    print(creating_a_string(first_string, second_string))
    print(creating_a_string(test_string1, test_string2))
    print(sort_list_of_int(test_list1, condition1))
    print(sort_list_of_int(test_list1, condition2))
    print(average_in_string(string1))
    print(average_in_string(string2))
    cheking_for_prime_numbers(test_number)
    cheking_for_prime_numbers(test_number1)
if __name__ == "__main__":
    main()

