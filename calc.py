operationCount = int(input("Введите кол-во повторений операции: "))
num1 = float(input("Введите первое число: "))

result = num1
for i in range(operationCount):
    operation = input("Введите операцию (+,-,*,/): ")
    num2 = float(input("Введите второе число: "))
    match(operation):
        case "+":
            result += num2
        case "-":
            result -= num2
        case "*":
            result *= num2
        case "/":
            if num2 == 0:
                print("Нельзя делить на 0!")
            else:
                result /= num2
        case _:
            print("Неверная операция")
    print(f"Итерация {i+1}: {result}")