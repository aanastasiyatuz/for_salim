import json

# загружаем бд из отдельных файлов с расширением json
with open("marketing_db.json") as file:
    try:
        marketing_db = json.load(file)
    except json.decoder.JSONDecodeError:
        marketing_db = {}
with open("director_db.json") as file:
    try:
        director_db = json.load(file)
    except json.decoder.JSONDecodeError:
        director_db = {}
with open("manager_db.json") as file:
    try:
        manager_db = json.load(file)
    except json.decoder.JSONDecodeError:
        manager_db = {}
with open("worker_db.json") as file:
    try:
        worker_db = json.load(file)
    except json.decoder.JSONDecodeError:
        worker_db = {}
with open("sale_manager_db.json") as file:
    try:
        sale_manager_db = json.load(file)
    except json.decoder.JSONDecodeError:
        sale_manager_db = {}

# проверка данных
def validate_password(account_db, account_type, login, password):
    if account_db.get(login):
        if account_db[login] == password:
            print("Вы успешно зашли!")
        else:
            print("Пароль не верный!")
            main()
    else:
        print(f"Такого юзера нет в отделе '{account_type}'!")
        main()

# login
def check_account(account_type, login, password):
    if account_type == 'маркетинг':
        validate_password(marketing_db, account_type, login, password)
    elif account_type == 'директор':
        validate_password(director_db, account_type, login, password)
    elif account_type == 'менеджер':
        validate_password(manager_db, account_type, login, password)
    elif account_type == 'работник':
        validate_password(worker_db, account_type, login, password)
    elif account_type == 'менеджерпродаж':
        validate_password(sale_manager_db, account_type, login, password)
    else:
        print("Такого типа аккаунта не существует!")
        main()

# register
def register_account(account_type, login, password, password_confirm):
    if password != password_confirm:
        print("Пароли не совпадают!")
        main()
        return

    if account_type == 'маркетинг':
        marketing_db[login] = password
        with open("marketing_db.json", 'w') as file:
            json.dump(marketing_db, file)
    elif account_type == 'директор':
        director_db[login] = password
        with open("director_db.json", 'w') as file:
            json.dump(director_db, file)
    elif account_type == 'менеджер':
        manager_db[login] = password
        with open("manager_db.json", 'w') as file:
            json.dump(manager_db, file)
    elif account_type == 'работник':
        worker_db[login] = password
        with open("worker_db.json", 'w') as file:
            json.dump(worker_db, file)
    elif account_type == 'менеджерпродаж':
        sale_manager_db[login] = password
        with open("sale_manager_db.json", 'w') as file:
            json.dump(sale_manager_db, file)
    else:
        print("Такого типа аккаунта не существует!")
        main()

# регистрация/авторизация
def main():
    account_type = input("Введите тип аккаунта\n (маркетинг, директор, менеджер, работник, менеджер продаж):\n").lower().replace(" ", '')
    enter = input("Вход или регистрация? (в/р): ").lower().strip()
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if enter == 'в':
        check_account(account_type, login, password)
    elif enter == 'р':
        password_confirm = input("Повторите пароль: ")
        register_account(account_type, login, password, password_confirm)

