import random
import string

# класс содержит функции, генерирующие email и пароли
# для логина в адресе электронной почты задала длину 8 символов, домены для генерации перечислены в списке
# для пароля ограничила длину от 6 до 10 символов
class Generator:
    def generate_login():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(['ya.ru', 'yandex.ru', 'mail.ru'])
        return f"{username}@{domain}"

    def generate_password():
        length = random.randint(6, 10)
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        return password