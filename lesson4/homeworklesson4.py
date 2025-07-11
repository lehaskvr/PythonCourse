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

def bubble_sort(list_to_sort:list[int], desc:bool = False) -> list[int]:
    for n in range(len(list_to_sort)):
        for a in range(len(list_to_sort) - n - 1):
            if list_to_sort[a] > list_to_sort[a + 1]:
                list_to_sort[a], list_to_sort[a + 1] = list_to_sort[a + 1], list_to_sort[a]
    if not desc:
        return list_to_sort
    else:
        return list_to_sort[::-1]
def average_in_string(s1:str) -> int:
    b = 0
    c = 0
    for n in s1:
        if n.isdigit():
            n = int(n)
            b += n
            c += 1
    if b == 0:
        print("Цифры не найдены")
    else:
        average = b / c
        print("Сумма цифр:", b, "Среднее арифмитическое:", average)

def cheking_for_prime_numbers(number1:int):
    for n in range(2, number1):
        if number1 % n == 0:
            print(f"Number {number1} isn't prime!")
            return
        else:
            continue
    print(f"Number {number1} is prime!")
	

def main():
    test_string1 = "hello"
    test_string2 = "world"
    first_string = "пока"
    second_string = "привет"
    test_list1 = [5, 2, 9, 1, 5, 6]
    desc = True
    desc1 =False
    string1 = "abc123def"
    string2 = "hello"
    test_number = 5
    test_number1 = 99
    print(creating_a_string(first_string, second_string))
    print(creating_a_string(test_string1, test_string2))
    print(bubble_sort(test_list1, desc))
    print(bubble_sort(test_list1, desc1))
    average_in_string(string1)
    average_in_string(string2)
    cheking_for_prime_numbers(test_number)
    cheking_for_prime_numbers(test_number1)
if __name__ == "__main__":
    main()

