global_phone_book = {}

menu_item = [
    'Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Добавить контакт',
    'Найти контакт',
    'Редактировать контакт',
    'Удалить контакт',
    'Выход'
]


def input_user_choice():
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return choice
        print('Введите пункт от 1 до 8')


def next_id(phone_book):
    if phone_book:
        return max(phone_book) + 1
    return 1


def open_file():
    """
    Функция открытия справочника
    """
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        data = sorted(file.readlines(), key=lambda x: x[0])
        data = list(map(lambda x: x.strip().split(';'), data))
        for contact in data:
            global_phone_book[next_id(global_phone_book)] = {'name': contact[0], 'phone': contact[1],
                                                             'comment': contact[2]}
        return global_phone_book


def show_contacts():
    if global_phone_book:
        print('=' * 66)
        for u_id, contact in global_phone_book.items():
            print(f'{u_id: >2}. {contact['name']: <20} {contact['phone']: <20} {contact['comment']: <20}')
        print('=' * 66)
    else:
        print('Телефонная книга пуста или не открыта')


def start():
    while True:
        print('Главное меню:')
        for i, item in enumerate(menu_item, 1):
            print(f'\t{i}. {item}')
        user_choice = input_user_choice()
        if user_choice == '1':
            if open_file():
                print('Телефонная книга успешно открыта')
            else:
                print('Телефонная книга пуста')
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            show_contacts()
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            pass
        elif user_choice == '6':
            pass
        elif user_choice == '7':
            pass
        elif user_choice == '8':
            print('До свидания')
            break


start()
