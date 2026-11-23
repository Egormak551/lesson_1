pocket_roulet = int(input("Введите номер кармана рулетки:"))

if(pocket_roulet <0) or (pocket_roulet >36):
    print("Вы ввели неверное число, введите число от 0 до 36.")
else:
    if(pocket_roulet == 0):
        print("Номер 0 равен зелёному карману рулетки.")
    #1-10
    elif(pocket_roulet > 0) and (pocket_roulet <= 10):
        if((pocket_roulet//2) == 0):
            print("Номер ",pocket_roulet," равен чёрному карману рулетки.")
        else:
            print("Номер ", pocket_roulet, " равен красному карману рулетки.")
    #11-18
    elif (pocket_roulet >= 11) and (pocket_roulet <= 18):
        if ((pocket_roulet // 2) == 0):
            print("Номер ", pocket_roulet, " равен красному карману рулетки.")
        else:
            print("Номер ", pocket_roulet, " равен чёрному карману рулетки.")
    #19-28
    elif (pocket_roulet >= 19) and (pocket_roulet <= 28):
        if ((pocket_roulet // 2) == 0):
            print("Номер ", pocket_roulet, " равен чёрному карману рулетки.")
        else:
            print("Номер ", pocket_roulet, " равен красному карману рулетки.")
    #29-36
    elif (pocket_roulet >= 29) and (pocket_roulet <= 36):
        if ((pocket_roulet // 2) == 0):
            print("Номер ", pocket_roulet, " равен красному карману рулетки.")
        else:
            print("Номер ", pocket_roulet, " равен чёрному карману рулетки.")