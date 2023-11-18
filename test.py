def show_data() -> None:
    """Выводит информацию из записной книжки notebook"""
    with open('D:\\python\\Intermediate control work\\notebook.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в записную книжку notebook."""
    index = input('Введите желаемый номер заметки: ')
    note = input('Введите заметку: ')
    with open('D:\\python\\Intermediate control work\\notebook.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{index}. {note}')


def change_data() -> None:
    """Изменяет информацию в записной книжке notebook."""
    index = input('Введите желаемый номер заметки: ')
    note = input('Введите заметку: ')
    with open('D:\\python\\Intermediate control work\\notebook.txt', 'r+', encoding='utf-8') as book:
        book.write(f'\n{index}. {note}')


def print_data() -> None:
    """Печатает результат поиска по тексту заметки в записной книжке """
    with open('D:\\python\\Intermediate control work\\notebook.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    note_to_find = input('Введите,что хотите найти: ')
    result = search(data, note_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска (фио\телефон)"""
    book = book.split('\n')
    result = [contact for contact in book if info.lower() in contact.lower()]
    return result


def change_ind() -> None:
    """Изменяет данные в выбранной строке по индексу"""
    with open('D:\\python\\Intermediate control work\\notebook.txt', 'r', encoding='utf-8') as read_file:
        data = read_file.readlines()
    
    note_to_find = input('Введите, что хотите найти: ')
    matching_indices = [index for index, line in enumerate(data) if note_to_find in line]

    if matching_indices:
        print(f'Заметка(-и) найдена(-ы) по индексам: {", ".join(map(str, matching_indices))}')
        mode = input('1. удалить, 2. изменить: ')

        if mode == '1':
            for note in reversed(matching_indices):
                data.pop(note)
            print('Заметка(-и) удалена(-ы)')

        elif mode == '2':
            index = input('Введите индекс желаемой заметки: ')
            text = input('Введите новый текст заметки: ')
            new_note = f'{index}. {text}\n'
            for note in matching_indices:
                data[note] = new_note
            print('Заметка(-и) изменена(-ы)')

        with open('D:\\python\\Intermediate control work\\notebook.txt', 'w', encoding='utf-8') as write_file:
            write_file.writelines(data)
    else:
        print('Нет совпадений')
