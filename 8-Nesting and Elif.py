print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age <=12:
        print("It's just $5.")
    elif age <=18:
        print("It's just $7.")
    else:
        print("It's just $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
