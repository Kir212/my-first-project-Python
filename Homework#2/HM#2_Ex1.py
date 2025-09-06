class Money:
    
    def __init__(self, name, rub=0, kop=0):
        self.name = name
        self.rub = 0
        self.kop = 0
        self.set_data(rub, kop)
    
    def set_data(self, rub, kop): 
        total_kop = rub * 100 + kop
        self.rub = total_kop // 100
        self.kop = total_kop % 100
        
    def get_info(self):
        total = self.rub + self.kop / 100
        print(f' {self.name}, Rub: {self.rub}, Kop: {self.kop:02d}')
        print(f'Total: {total:.2f} руб.')

    def add_money(self, rub, kop):
        total_kop = (self.rub * 100 + self.kop) + (rub * 100 + kop)
        self.set_data(0, total_kop)

    def sub_money(self, rub, kop):
        current_balance = self.rub * 100 + self.kop
        amount_to_subtract = rub * 100 + kop
        
        if current_balance < amount_to_subtract:
            print("Недостаточно средств для операции!")
            return False

        new_balance = current_balance - amount_to_subtract
        self.set_data(0, new_balance)
        return True

    def sent_cash_back(self, procent: float):
        current_balance = self.rub * 100 + self.kop
        cash_back = current_balance * procent
        # Округляем до целых копеек
        cash_back = round(cash_back)
        new_balance = current_balance + cash_back
        self.set_data(0, new_balance)

    def transfer_to(self, target_account, rub, kop):
        """
        Перевод денег с текущего счета на целевой счет
        
        :param target_account: Объект Money, на который переводятся средства
        :param rub: Количество рублей для перевода
        :param kop: Количество копеек для перевода
        :return: True если перевод успешен, False если нет
        """
        # Проверяем, достаточно ли средств на текущем счете
        if not self.sub_money(rub, kop):
            print(f"Ошибка перевода: недостаточно средств на счете '{self.name}'")
            return False
        
        # Добавляем средства на целевой счет
        target_account.add_money(rub, kop)
        print(f"Успешно переведено {rub} руб. {kop} коп. с '{self.name}' на '{target_account.name}'")
        return True


# Пример использования
new_wallet1 = Money("Счет№1", 100, 20)
new_wallet2 = Money("Счет№2", 100, 20)

print("Начальное состояние:")
new_wallet1.get_info()
new_wallet2.get_info()

# Добавляем деньги на первый счет
new_wallet1.add_money(5, 25)
print("\nПосле добавления 5 руб. 25 коп. на Счет№1:")
new_wallet1.get_info()

# Снимаем деньги с первого счета
new_wallet1.sub_money(12, 25)
print("\nПосле снятия 12 руб. 25 коп. с Счет№1:")
new_wallet1.get_info()

# Начисляем кэшбэк на первый счет
new_wallet1.sent_cash_back(0.02)
print("\nПосле начисления кэшбэка 2% на Счет№1:")
new_wallet1.get_info()

# Начисляем кэшбэк на первый счет
new_wallet1.sent_cash_back(0.03)
print("\nПосле начисления кэшбэка 3% на Счет№1:")
new_wallet1.get_info()

# Переводим деньги с первого счета на второй
print("\nПопытка перевода 50 руб. 50 коп. с Счет№1 на Счет№2:")
new_wallet1.transfer_to(new_wallet2, 50, 50)

print("\nСостояние после перевода:")
new_wallet1.get_info()
new_wallet2.get_info()

# Пытаемся перевести больше, чем есть на счете
print("\nПопытка перевода 500 руб. 50 коп. с Счет№1 на Счет№2:")
new_wallet1.transfer_to(new_wallet2, 500, 50)

print("\nФинальное состояние:")
new_wallet1.get_info()
new_wallet2.get_info()