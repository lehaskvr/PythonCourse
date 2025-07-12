text = 'tigers are orange animals they eat other animals'

def unique_words(text: str) -> set:
    words = text.split()
    result_set = set(words)
    return len(result_set)
print(unique_words(text))
