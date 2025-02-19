class User: #Создаем пользователя
    def __init__(self, user_id, name): #Конструктор
        self._user_id = user_id
        self._name = name
        self._access_level = 'пользователь'

    # Геттеры
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттеры
    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"Пользователь(ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'Администратор'
        self._users_list = []

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f"Пользователь {user.get_name()} Успешно добавлен.")
        else:
            print("Неверный тип объекта.")

    # Метод для удаления пользователя
    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"Пользователь с ID {user_id} успешно удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для отображения всех пользователей
    def list_users(self):
        if not self._users_list:
            print("Список пользователей пуст.")
        else:
            for user in self._users_list:
                print(user)


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Администратор Иван")

    # Создаем обычных пользователей
    user1 = User(2, "Алиса")
    user2 = User(3, "Вова")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Выводим список пользователей
    admin.list_users()

    # Администратор удаляет пользователя
    admin.remove_user(2)

    # Снова выводим список пользователей
    admin.list_users()