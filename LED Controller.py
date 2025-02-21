brightness = 50

while True:
    print("-----++LED BRIGHTNESS CONTROLLER-----")
    print(f"Brightness: {brightness}% [{'|' * (brightness // 2)}]")
    command = input("Enter + to increase, - to decrease: ").strip()
    if command == '+':
        if brightness < 100:
            brightness += 10
        else:
            print("Maximum brightness reached!")
    elif command == '-':
        if brightness > 10:
            brightness -= 10
        else:
            print("Minimum brightness reached!")
    else:
        print("Invalid input! Enter only + or -")