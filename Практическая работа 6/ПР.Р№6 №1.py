print("Вводные данные о здоровье:")
temp_now = float(input("Введите свою теспературу:"))
pressure_now = float(input("Введите своё давление:"))
pulse_now = float(input("Введите свой пульс:"))
temp_status = 0
pressure_status = 0
pulse_status = 0

print("Анализ здоровья...")

# Температура

if (temp_now >= 36) and (temp_now <= 37):
    temp_status = 1
    print("Температура в порядке.")
elif ((temp_now >= 35)and(temp_now < 36))  or ((temp_now > 37)and(temp_now <= 38 )):
    temp_status = 2
    print("Температура не критично отходит от нормы.")
else:
    temp_status = 3
    print("Температура критично отходит от нормы.")

# Давление

if (pressure_now >= 110) and (pressure_now <= 130):
    pressure_status = 1
    print("Давление в норме.")
elif ((pressure_now >= 105)and(pressure_now < 110))  or ((pressure_now > 130)and(pressure_now <= 140 )):
    pressure_status = 2
    print("Давление не критично отходит от нормы.")
else:
    pressure_status = 3
    print("Давление критично отходит от нормы.")

# Пульс

if (pulse_now >= 60) and (pulse_now <= 100):
    pulse_status = 1
    print("Пульс в норме.")
elif ((pulse_now >= 55)and(pulse_now < 60))  or ((pulse_now > 100)and(pulse_now <= 110 )):
    pulse_status = 2
    print("Пульс не критично отходит от нормы.")
else:
    pulse_status = 3
    print("Пульс критично отходит от нормы.")

# Проверка
if (temp_status == 1) and (pressure_status == 1) and (pulse_status == 1):
    print("Ваше состояние (в норме).")
elif ((temp_status == 2) or (pressure_status == 2) or (pulse_status == 2))  and ((temp_status != 3) or (pressure_status != 3) or (pulse_status != 3)):
    print("Ваше состояние (Лёгкое недомогание).")
elif (temp_status == 3) or (pressure_status == 3) or (pulse_status == 3):
    print("Ваше состояние (Не в норме) Требуется осмотр врача.")