# a = 2


# print("Result ", a)

# m = "Incorrect"
# output_string = f"Result {m}"

# print(output_string)


# h = 1

# # while h < 50:

# #     if h % 2:
# #         print("h is odd")
# #     else:
# #         print("h is even")

# #     h += 1


# while True:
#     data = int(input("Enter the number: "))

#     if data == 5:
#         break

#     data += 2

#     print(f"Result is {data}")


# a = {}

# a["one"] = 2

# print(a["one"])


# Ouput
# {"chars": 12, "symbols": 2, "digits": 9}

# def count_characters(example: str) -> dict:
#     result = {"chars": 0, "symbols": 0, "digits": 0}
#     for n in example:
#         if n.isalpha():
#             result["chars"] += 1
#         elif n.isdigit():
#             result["digits"] += 1
#         else:
#             result["symbols"] += 1
#     return result


# def main():
#     example_string = "SSS12$%"
#     print(f"Result is {count_characters(example_string)}")

# if __name__ == "__main__":
#     main()



####################################################

# result = {
#     key : value,
#     key1 : value,
#     key2: value1
# }

# result[key] 
# result[key2] = value1

def count_of_symbols(example_string: str) -> dict:
    result = {}
    for n in example_string:
        if n in result.keys(): # result.values()
            result[n] += 1
        else:
            result[n] = 1
    return result

    # for key, value in result.items()
        

print(count_of_symbols("Hello, World!"))


def dict_of_symbols(example_string: str) -> dict:
    result = {"n[0]": 0, "n[1]": 0, "n[2]": 0}
    for n in example_string:
        if n == example_string[0]:
            result["n[0]"] += 1
        if n == example_string[1]:
            result["n[1]"] += 1
        if n == example_string[2]:
            result["n[2]"] += 1
    return result


def main():
    example_string = "Hello, World"
    print(f"Result is {dict_of_symbols(example_string)}")

if __name__ == "__main__":
    main()
            

####################################

def search_for_word(example_word: str, example_string: str) -> int:
    text = example_string.split()
    print(text)
    for t in text:
        print(t)
        if example_word == t:
            index = 0
            for t1 in text:
                print(t1)
                if t1 == t:
                    break
                index += len(t1) + 1

    return index

print(search_for_word("the", "hello the best World!"))

# def main():
#     example_word = "the"
#     example_string = "hello the best World!"
#     print(f"Result is {search_for_word(example_word, example_string)}")

# if __name__ == "__main__":
#     main()



##################################################



def replace_words(text: str, words_to_replace: list, word_replacer: str) -> str:
    a = text.split()
    for n in a:
        if n in words_to_replace:
            text = text.replace(n, word_replacer)

    return text



def main():
    text = "apple orange banana kiwi"
    words_to_replace = ["apple", "banana", "kiwi"]
    word_replacer = "K"
    print(f"Результат: {replace_words(text, words_to_replace, word_replacer)}")

if __name__ == "__main__":
    main()