import json

users = {}

def add_user():
    login = input("Введіть логін :: ")
    if login in users:
        print("Користувач із таким логіном вже існує")
    else:
        users[login] = input("Введіть пароль :: ")
        print(f"Користувача '{login}' додано")

def delete_user():
    login = input("Введіть логін для видалення :: ")
    if users.pop(login, None):
        print(f"Користувача '{login}' видалено")
    else:
        print(f"Користувача '{login}' не знайдено")

def change_password():
    login = input("Введіть логін :: ")
    if login not in users:
        print(f"Користувача '{login}' не знайдено")
        return
    new_password = input("Введіть новий пароль :: ")
    if users[login] == new_password:
        print("Новий пароль не може бути таким самим, як старий")
    else:
        users[login] = new_password
        print("Пароль успішно змінено")

def check_weak_passwords():
    print("\nНезахищені паролі ::")
    weak = {login: pwd for login, pwd in users.items() if len(pwd) < 6 or pwd.isalpha()}
    if weak:
        for login, pwd in weak.items():
            print(f"Логін :: {login}, Пароль :: {pwd}")
    else:
        print("Усі паролі захищені")

def get_password_by_login():
    login = input("Введіть логін :: ")
    print(f"Пароль: {users.get(login, 'Користувача не знайдено')}")

def save_users_to_file():
    with open("users.json", "w") as file:
        json.dump(users, file)
    print("Список користувачів збережено у файл")

def user_management():
    actions = {
        "1": add_user,
        "2": delete_user,
        "3": change_password,
        "4": check_weak_passwords,
        "5": get_password_by_login,
        "6": save_users_to_file,
        "7": exit,
    }
    while True:
        print("\nМеню:")
        print("1. Додати нового користувача")
        print("2. Видалити користувача")
        print("3. Змінити пароль")
        print("4. Перевірити паролі")
        print("5. Отримати пароль за логіном")
        print("6. Зберегти список користувачів у файл")
        print("7. Вийти")
        choice = input("Виберіть дію (1-7) :: ")
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Try again !!!")

user_management()