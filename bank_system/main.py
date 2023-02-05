all_data = []
bank_accounts = []
account_in_system = []

# Чтение всех данных из файла (Номер счета, пин код, баланс)
with open('data_base.txt', 'r') as file:
    all_data = file.readlines()
all_data = [[int(n) for n in x.split()] for x in all_data]
print(all_data)

#Получение всех банковских счетов
for i in range(0, len(all_data)):
    bank_accounts.append(all_data[i][0])
print(bank_accounts)

def registration():
    print("Регистрация")

def authorization():
    print("Авторизация")

def balance():
    print("Баланс")

def deposit_money():
    print("Пополнить счет")

def withdraw_money():
    print("Снять со счета")



