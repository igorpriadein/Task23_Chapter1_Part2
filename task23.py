# Напишите функцию котрый будет определять введенный год, высокосный или нет.

year = int(input("vvedite god: "))
if year % 4 == 00 and year % 100 != 0:
    print("visokostnii")
else:
    print("net")