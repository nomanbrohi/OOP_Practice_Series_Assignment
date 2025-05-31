# Decorator function without parameters acceptance
def log_function_call(func):
    def wrapper():
        print("function is being called")
        return func()
    return wrapper()

@log_function_call
def say_hello():
    print("Hello World")

# Decorator function with parameters acceptance

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Noman")