import smtplib

EMAIL = "k.brantova2015@yandex.ru"
PASSWORD = "hohtcsufjcrwpdll"

try:
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(EMAIL, PASSWORD)
    print("Авторизация успешна!")
except Exception as e:
    print("Ошибка авторизации:", e)
finally:
    server.quit()
