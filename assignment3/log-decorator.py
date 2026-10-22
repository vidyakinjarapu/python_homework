# -------------------- TASK 1 -------------------------

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = list(args) if args else None
        keyword = list(args) if kwargs else None

        record = (
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
        )
        logger.log(logging.INFO, record)
        # print(result)
        return result
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

@logger_decorator
def greet(name = "Vidya"):
    return f"Hello, {name}"

@logger_decorator
def describe(item, color):
    return f"{item} is {color}"

@logger_decorator
def greet2():
    return ""


add(2, 3)
greet("CTD")
describe("sky", color="blue")
greet2()