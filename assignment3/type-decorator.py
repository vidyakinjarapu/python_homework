# ----------------- TASK 2 -------------------

def type_converter(type_of_output):
    def out_decorator(func):
        def wrapper(*args, **kwargs):
            out = func(*args, **kwargs)
            return type_of_output(out)
        return wrapper
    return out_decorator

@type_converter(str)
def return_int():
   return 5

@type_converter(int)
def return_string():
   return "not a number"

y = return_int()
# print(f"y is {y}")
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!")