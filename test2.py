import test


while True:
    print('1. вывод, 2. добавление, 3. поиск, 4.замена/удаление book2')
    mode = int(input())
    if mode == 1:
        test.show_data()
    elif mode == 2:
        test.add_data()
    elif mode == 3:
        test.print_data()
    elif mode == 4:
        test.change_ind()
    else:
        break