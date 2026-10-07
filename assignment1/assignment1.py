# Write your code here.
# Task 1
def hello():
    print("Hello!")
    return "Hello!"
# Task 2
def greet(name):
    return f'Hello, {name}!'
# Task 3
def calc(a, b, f="multiply"):
    try:
        a = float(a)
        b = float(b)
    except Exception as e:
        return "You can't multiply those values!"
    try:
        if f == "multiply":
            return a * b
        elif f == "add":
            return a + b
        elif f == "modulo":
            return a % b
        elif f == "subtract":
            return a - b
        elif f == "divide":
            return a / b
        elif f == "int_divide":
                return a // b
        elif f == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"

# Task 4
def data_type_conversion(value, data_type):
    try:
        return eval(data_type)(value)
    except:
        return f'You can\'t convert {value} into a {data_type}.'

# Task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg > 90:
            return "A"
        elif avg > 80:
            return "B"
        elif avg > 70:
            return "C"
        elif avg > 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."

# Task 6
def repeat(word, number):
    f_str = ""
    for i in range(number):
        f_str = f_str + word
    return f_str

# Task 7
def student_scores(fun, **kwargs):
    for key, value in kwargs.items():
        if fun == "mean":
            avg = sum(kwargs.values())/ len(kwargs.values())
            return avg
        elif fun == "best":
            max_key = max(kwargs, key=kwargs.get)
            return max_key
        else:
            return "Invalid input"
# print(student_scores("best", Tom=75, Dick=89, Angela=91))

# Task 8
def titleize(sentence):
    small_words = ["a", "on", "an", "the", "of", "and", "is","in"]
    words = sentence.split(" ")
    final_words = []
    last_word_index = len(words) - 1
    for i, word in enumerate(words):
        if word not in small_words or i == 0 or i == last_word_index:
            word = word.capitalize()
            final_words.append(word)
        else:
            final_words.append(word)

    final_sentence = " ".join(final_words)
    return final_sentence

# Task 9
def hangman(secret, guess):
    alpha_list = []
    for char in secret:
        if char in guess:
            alpha_list.append(char)
        else:
            alpha_list.append('_')
    # print("list is: ", alpha_list)
    return "".join(alpha_list)

def pig_latin(sentence):
    fi_words = []
    words = sentence.split(" ")
    vowels = "aeiou"
    for word in words:
        if word[0] in vowels:
            fi_words.append(word + "ay")
        else:
            vowel_index = -1
            for i, char in enumerate(word):
                if char in vowels: 
                    if char == "u" and i > 0 and word[i - 1] == "q":
                        continue
                    vowel_index = i
                    break

            if vowel_index != -1:
                fi_words.append(word[vowel_index:] + word[:vowel_index] + "ay")
            else:
                fi_words.append(word + "ay")

    return " ".join(fi_words)
print(pig_latin("apple"))