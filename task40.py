# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные
#  каналы.
#  Требования:
#  Базовый класс NotificationSender с методом send(message, user).
#  Дочерние классы:
#  EmailSender: отправляет email с темой "Образовательная платформа"
#  SMSSender: отправляет SMS (первые 50 символов сообщения)
#  PushSender: отправляет push-уведомление с иконкой "🎓"
#  Класс пользователя User:
#  Свойства: name, preferred_notifications (список объектов NotificationSender)


# Этот код должен работать после релизации:
#user = User("Мария", [EmailSender(), PushSender()])
#notify_user(user, "Блок аналитики начинается с 27 октября!")

#def notify_user(user, message):
    #for sender in user.preferred_notifications:
        #sender.send(message, user)
        
class NotificationSender:
    def send(self, message, user):
        raise NotImplementedError("Метод send должен быть реализован в дочерних классах")

class EmailSender(NotificationSender):
    def send(self, message, user):
        print(f"Email для {user.name}:")
        print(f"Тема: Образовательная платформа")
        print(f"Текст: {message}")
        print("-" * 40)  # Исправлено: \" → "

class SMSSender(NotificationSender):
    def send(self, message, user):
        truncated_message = message[:50]
        print(f"SMS для {user.name}:")
        print(f"Текст: {truncated_message}")
        print("-" * 40)  # Исправлено: \" → "

class PushSender(NotificationSender):
    def send(self, message, user):
        print(f"Push-уведомление для {user.name}:")
        print(f"Иконка: 🎓")
        print(f"Текст: {message}")
        print("-" * 40)  # Исправлено: \" → "

class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications

def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)

user = User("Мария", [EmailSender(), PushSender()])
notify_user(user, "Блок аналитики начинается с 27 октября!")
