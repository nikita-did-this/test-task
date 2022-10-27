class ScreeningMail:
    def __init__(self, screening_symbol="x"):
        self.screening_symbol = str(screening_symbol)

    def screening(self, mail):
        if not mail:
            raise ValueError("введите почту для экранирования")
        elif "@" not in mail:
            raise ValueError("введите почту для экранирования")
        elif mail[-1] == "@":
            raise ValueError("введите почту для экранирования")

        mail_list = mail.split('@')
        screened_part = mail_list.pop(0)
        mail_list.insert(0, self.screening_symbol * len(screened_part))
        return "@".join(mail_list)


class ScreeningPhone:
    def __init__(self, screening_symbol, char_amount=3):
        self.screening_symbol = str(screening_symbol)
        self.char_amount = int(char_amount)

    def screening(self, phone):
        if not phone.isdigit():
            raise ValueError("Введите номер телефона")

        char_amount = self.char_amount
        screened_phone = str()
        for index in reversed(range(len(phone))):
            if char_amount != 0 and phone[index] != " ":
                screened_phone += self.screening_symbol
                char_amount -= 1
            else:
                screened_phone += phone[index]

        screened_phone = screened_phone[::-1].split(" ")
        while '' in screened_phone:
            screened_phone.remove('')
        return ' '.join(screened_phone)


class ScreeningSkype:
    @staticmethod
    def screening(skype_ref):
        if not skype_ref:
            raise ValueError("Вы передали пустую строку")
        skype_ref_split = skype_ref.split('skype:')
        username = skype_ref_split[1].split("?")
        skype_ref = skype_ref.replace(username[0], "xxx")
        return skype_ref
