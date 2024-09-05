def check_address(adress):
    global check_bool
    if '@' not in adress:
            check_bool = False
    elif adress[len(adress) - 3:] != '.ru' and adress[len(adress) - 4:] != '.com' and adress[len(adress) - 4:] != '.net':
        check_bool = False

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    global check_bool
    check_bool = True
    check_address(recipient)
    check_address(sender)
    if check_bool == False:
        print('Невозможно отправить письмо с адреса ' + sender + " на адрес " + recipient )
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса ' + sender + " на адрес " + recipient)
    else: print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес' + recipient)

check_bool = True
send_email('Это сообщение для пароверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста,, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')