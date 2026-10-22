# -------------------- TASK 1 -------------------------

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = list(args) if args else None
        keyword = dict(kwargs) if kwargs else "none"

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
    return True

@logger_decorator
def greet(name = "Vidya"):
    return logger_decorator

@logger_decorator
def describe(item, color="pink"):
    return f"{item} is {color}"

@logger_decorator
def greet2():
    return "nothing"


add(2, 3)
greet("CTD")
describe("sky", color="blue")
greet2()