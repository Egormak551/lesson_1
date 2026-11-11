print("Введите своё место")
m = int(input())
if m>0 and m<=36:
    if m%4 == 0:
        print("Ваше место:",m//4)
    else:
        print("Ваше место:",(m//4)+1)
else:
    print("Введенно неверное место")