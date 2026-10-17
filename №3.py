#Функция помогает определить, как можно расфасовать пирожные.
def print_pack_report():

    #Принимает число пирожных пользователя.
    amount = int(input("Введите количество пирожных."))
    #amount - количество пирожных.

    #Советует, как расфасовать пирожные.
    if amount <= 1:
        print("Введите число пирожных больше одного!")
    elif amount % 3 == 0 and amount % 5 == 0:
        print(f"{amount} - расфасуем по 3 или по 5")
    elif amount % 5 == 0 and not (amount % 3 == 0):
        print(f"{amount} - расфасуем по 5")
    elif amount % 3 == 0 and not (amount % 5 == 0):
        print(f"{amount} - расфасуем по 3")
    else:
        print(f"{amount} - не заказываем!")

print_pack_report()