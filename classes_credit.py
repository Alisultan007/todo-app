class Card:
    def __init__(self, card_number, card_holder_name, expiration_month, card_expiration_year):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiration_month = expiration_month
        self.card_expiration_year = card_expiration_year
        self.__act_on = False

    def __str__(self):
        return f'Card: {self.card_number}  {self.card_holder_name}  {self.expiration_month}  {self.card_expiration_year}'

    def get_act_status(self):
        if self.__act_on:
            return ("Карта работает")
        else:
            return ("Карта заблокирована")

    def set_act_status(self, status):
        if self.__act_on == status:
            return f"Карта имеет статус {status}"
        else:
            self.__act_on = status
            return f"Карта изменина на статус {status}"


if __name__ == '__main__':
    card1 = Card("77777777", ":Kaspi", 12, 2025)
    print(card1)
    # print(type(card1))
    card1.make = "Halyk"

    print(card1)
    print(card1.get_act_status())
    print(card1.set_act_status(True))
    print(card1.get_act_status())
