
print('bKash')
print('1 Send Money')
print('2 Send Money To Non-bKash User')
print('3 Mobile Recharge')
print('4 Payment')
print('5 Cash Out')
print('6 Pay Bill')
print('7 Microfinance')
print('8 Download bKash App')
print('9 My bKash')
print('10 Reset PIN')
prompt = int(input())

if prompt == 1 :
    print('Enter Receiver bKash Account No:')
    number = int(input())
    if number:
        print('FREE Send Money to 5 Priyo Numbers')
        print('Dial *247# and select number 9 to find priyo Numbers.')
        print('Enter Amount')
        amount = int(input())
        if amount:
            print('FREE Send Money to 5 Priyo numbers up to 25,000 Tk. every month.')
            refer = input('Enter Reference: ')
            if refer:
                print('Add up to 5 Priyo Numbers to Send Money for FREE.')
                print('Send Money')
                print(f'To: {number} ')
                print(f'Amount: Tk {amount}')
                print(f'Reference: {refer}')
                PIN = int(input('Enter Menu PIN to confirm:'))
                if PIN:
                    print('Your payment is Successfull')
elif prompt == 2:
    number = int(input('Enter Reference Number:'))
    if number:
        amounts = int(input('Enter Amount:'))
        if amounts:
            referen = input('Enter Reference: ')
            if referen:
                print('Send Money to Non-bKash User: ')
                print(f'To : {number}')
                print(f'Amount : {amounts}')
                print(f'Reference : {referen}')
                PINS = int(input('Enter Menu PIN to confirm: '))
                if PINS:
                    print('Your Money Succesfully send')
