first_number = int(input("Введите первое значение"))
Operation = input("Введите необходимую операцию |+|-|*|/| ")
Second_number = int(input("Введите второе значение"))

match Operation:
    case "+" :
        print("Ответ:",first_number + Second_number)
    case "-" :
        print("Ответ:",first_number - Second_number)
    case "*" :
        print("Ответ:",first_number * Second_number)
    case "/" :
        print("Ответ:",first_number / Second_number)
    case _ :
        print("Введена неверная операция")