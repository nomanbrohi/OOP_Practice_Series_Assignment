class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Access Granted.")

try:
    userInput = input("Please Enter Your age: ")
    check_age(int(userInput))

except InvalidAgeError as e:
    print(f'InvalidAgeError Caught: {e}')
except ValueError:
    print("Please Enter valid number")