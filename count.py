try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age % 2 == 0:
        print("Your age is", age)
        print("Your age is EVEN.")
    else:
        print("Your age is", age)
        print("Your age is ODD.")

except ValueError:
    print("Error: Please enter a valid whole number for your age.")

except SyntaxError:
    print("Error: Please enter your age correctly.")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("Age Counter program has finished.")
