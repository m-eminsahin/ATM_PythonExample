accountEmin = {
'name': 'Emin Sahin',
'accountNumber': '150354',
'balance': 3600,
'overdraftAccount': 1700
}

accountEzgi = {
'name': 'Ezgi Ates',
'accountNumber': '232733',
'balance': 6600,
'overdraftAccount': 3000
}

accountAli = {
'name': 'Ali Cetin',
'accountNumber': '142448',
'balance': 12000,
'overdraftAccount': 0
}

def withdraw_money(account, balance):
    print("Welcome, {}".format(account['name']))

    if account['balance'] >= amount:
        account['balance'] -= amount
        print('You can take your money.')
        check_balance(account)
    else:
        total = account['balance'] + account['overdraftAccount']
        if total >= amount:
            overdraft_usage = input('Use overdraft account? (yes/no)')

            if overdraft_usage == 'yes':
                overdraft_amount = amount - account['balance']
                account['balance'] = 0
                account['overdraftAccount'] -= overdraft_amount
                print('You can take your money.')
                check_balance(account)
            else:
                print(
                    "Your account number {} has a balance of {}.".format(account['accountNumber'], account['balance']))
        else:
            print("Sorry, your balance is insufficient.")
            check_balance(account)


def check_balance(account):
    print("Your account number {} has a balance of {}. Your overdraft account balance is {}.".format(account['accountNumber'], account['balance'], account['overdraftAccount']))

amount = 5000
withdraw_money(accountEmin, amount)
check_balance(accountEmin)

print('******************************************************')

amount = 3000
withdraw_money(accountEmin, amount)
check_balance(accountEmin)