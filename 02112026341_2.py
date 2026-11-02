#Список
my_list = [1 , 2 ,3]
print(my_list)
my_list[0] = 100
print(my_list)

#Кортеж
my_tuple = [1, 2, 3]
print(my_tuple)
try:
    my_tuple[0] = 100
    print(my_tuple)
except TypeError:
    print("Кортеж не меняется")

#Список
my_string = "Cat"
print(my_string)
try:
    my_string[0] = 'b'
except TypeError:
    print("Строка не меняется")