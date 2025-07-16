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
    
def average_in_string(s1:str) -> tuple[int, float] | None:
    b = 0
    c = 0
    for n in s1:
        if n.isdigit():
            b += int(n)
            c += 1
    if b == 0:
        return 
    else:
        average = b / c
        return b, average

def is_prime(number1:int) -> bool:
    for n in range(2, number1):
        if number1 % n == 0:
            return
        else:
            continue
    return True
	
def intersection_of_sets(set1:set, set2:set) -> tuple[set, set]:
    common = set.intersection(set1, set2)
    set1 = set.difference(set1, set2)
    return common, set1
    

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
    test_set = {1, 2, 3, 4, 5}
    test_set1 = {4, 5, 6, 7}
    test_set2 = {99, 67, 103, 44, 22, 1, 0}
    test_set3 = {99, 103, 0, 56, 23}
    print(creating_a_string(first_string, second_string))
    print(creating_a_string(test_string1, test_string2))
    print(bubble_sort(test_list1, desc))
    print(bubble_sort(test_list1, desc1))
    if average_in_string(string1):
        sum, ave = average_in_string(string1)
        print(f"Сумма цифр: {sum},  среднее арифмитическое: {ave} ")
    else:
        print("Цифры не найдены")
    if average_in_string(string2):
        sum1, ave1 = average_in_string(string2)
        print(f"Сумма цифр: {sum1}, среднее арифмитическое: {ave1}")
    else:
        print("Цифры не найдены")
    if is_prime(test_number):
        print(f"Number {test_number} is prime!")
    else:
        print(f"Number {test_number} isn't prime!")
    if is_prime(test_number1):
        print(f"Number {test_number1} is prime!")
    else:
        print(f"Number {test_number1} isn't prime!")
    set1, set2 = intersection_of_sets(test_set, test_set1)
    set3, set4 = intersection_of_sets(test_set2, test_set3)    
    print(f"Пересечение списков: {set1}, новый первый список: {set2}")
    print(f"Пересечение списков: {set3}, новый первый список: {set4}")
if __name__ == "__main__":
    main()

