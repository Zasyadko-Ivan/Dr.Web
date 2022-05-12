import os

file_type = input("Выберите расширение файла: \n test.csv - укажите csv (по умолчанию) \n test.list - укажите list \n test.txt - укажите txt \n test.table - укажите table:  ")
driver_type = input("Выберите тип драйвера: \n File System - укажите F (по умолчанию) \n Kernel - укажите K:  ")
print("\n")

if file_type == "csv" or file_type == ".csv" or file_type == '':

    os.system("driverquery /fo csv > test.csv")

    print('Файл test.csv создан')
    print('\n')

    name_file = 'test.csv'

    my_file = open(name_file, mode='r', encoding='utf-8')

    if driver_type == "F" or driver_type == 'f' or driver_type == '':
        for line in my_file:
            if line.count('"File System "'):
                print(line.strip())
    elif driver_type == "K" or driver_type == "k":
        for line in my_file:
            if line.count('"Kernel "'):
                print(line.strip())
    else:
        print("Указанный", driver_type, "тип драйвера не реализован в этом скрипте")

    my_file.close()

elif file_type == "list" or file_type == ".list":

    os.system("driverquery /fo list > test.list")

    print('Файл test.list создан')
    print('\n')

    name_file = 'test.list'

    my_file = open(name_file, mode='r', encoding='utf-8')

    if driver_type == "F" or driver_type == 'f' or driver_type == '':
        i = 0
        for line in my_file:
            if line.count("Module Name:"):
                module_name = line.strip()
            if line.count("Display Name:"):
                display_name = line.strip()
            if line.count('Driver Type:       File System') == 1:
                driver_type = line.strip()
                i += 1
            if line.count('Link Date:') and i == 1:
                link_date = line.strip()
                print(module_name, display_name, driver_type, link_date, sep="\n")
                print('\n')
                i -= 1
    elif driver_type == "K" or driver_type == "k":
        i = 0
        for line in my_file:
            if line.count("Module Name:"):
                module_name = line.strip()
            if line.count("Display Name:"):
                display_name = line.strip()
            if line.count('Driver Type:       Kernel') == 1:
                driver_type = line.strip()
                i += 1
            if line.count('Link Date:') and i == 1:
                link_date = line.strip()
                print(module_name, display_name, driver_type, link_date, sep="\n")
                print('\n')
                i -= 1
    else:
        print("Указанный", driver_type, "тип драйвера не реализован в этом скрипте")

    my_file.close()

elif file_type == "txt" or file_type == ".txt":

    os.system("driverquery > test.txt")

    print('Файл test.txt создан')
    print('\n')

    name_file = 'test.txt'

    my_file = open(name_file, mode='r', encoding='utf-8')

    if driver_type == "F" or driver_type == 'f' or driver_type == '':
        for line in my_file:
            if line.count('File System'):
                print(line.strip())
    elif driver_type == "K" or driver_type == "k":
        for line in my_file:
            if line.count('Kernel'):
                print(line.strip())
    else:
        print("Указанный", driver_type, "тип драйвера не реализован в этом скрипте")

    my_file.close()

elif file_type == "table" or file_type == ".table":

    os.system("driverquery /fo table > test.table")

    print('Файл test.table создан')
    print('\n')

    name_file = 'test.table'

    my_file = open(name_file, mode='r', encoding='utf-8')

    if driver_type == "F" or driver_type == 'f' or driver_type == '':
        for line in my_file:
            if line.count('File System'):
                print(line.strip())
    elif driver_type == "K" or driver_type == "k":
        for line in my_file:
            if line.count('Kernel'):
                print(line.strip())
    else:
        print("Указанный", driver_type, "тип драйвера не реализован в этом скрипте")

    my_file.close()

else:
    print('Файл с расширением', file_type, 'невозможно создать')

