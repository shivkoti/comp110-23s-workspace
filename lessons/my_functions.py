"""Things I'll Be Importing"""

def addition(x: int, y: int):
    return x + y


my_variables: str = "Hello!"


if __name__ == "__main__":
    print("This should only print when running my_functions")
else:
    print("my_functions is being imported")