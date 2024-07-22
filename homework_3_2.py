def send_email(massege = 'Пожалуйста, исправьте задание', recipient = 'urban.student@mail.uk', sender='urban.teacher@mail.uk'):
    if ((".net") in sender) or ((".com") in sender) or ((".ru") in sender) or (("@") in sender):
        if ((".net") in recipient) or ((".com") in recipient) or ((".ru") in recipient) or (("@") in recipient):
            if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
            elif sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")
        else:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")

send_email()
