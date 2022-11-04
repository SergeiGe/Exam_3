# 1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами,
# остальные заменены на звездочки, CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

card_number = input('Введите номер карты: ')
cvc_code = input('Введите CVC-код: ')
pin_code = input('Введите PIN-код: ')

def display_data_card_hide(number, cvc, pin):
    number_hide = number[0:4] + '*' * len(number[4:])
    cvc_hide = '#' * len(cvc)
    pin_hide = '&' * 3 + pin[-1]
    print('-------------------------------------')
    print('Данные вашей карты:')
    print('Номер карты: ', number_hide)
    print('CVC-код карты: ', cvc_hide)
    print('PIN-код карты: ', pin_hide)


display_data_card_hide(card_number, cvc_code, pin_code)