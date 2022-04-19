# Name: Gurnaman Singh
# ID: 010851677 

from multiprocessing.sharedctypes import Value
import socket
s = socket.socket()
port = 56789
s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())

while True:
    print("0) Exit")
    print("1) Deposit money into the account on the server.")
    print("2) Withdraw money from the account on the server.")
    print("3) Check the balance of the amount in the account on the server.\n")
    Option = input("Type In The Operation Number From The List That You Would Like To Perform: ")

    
    if(Option == '0'):
        s.send(bytes(f'{Option} {0}', 'utf-8'))
        break
    elif(Option == '1'):
        try:
            amountDeposit = input("Enter The Amount You Would Like To Deposit: ")
            while(int(amountDeposit)<0 or amountDeposit.isalpha()):
                print('\n***Amount Must Be Greater Than 0 And Float & Character Values Are Not Allowed***\n')
                amountDeposit = input("Enter The Amount You Would Like To Deposit: ")
            s.send(bytes(f'{Option} {amountDeposit}', 'utf-8'))
            print(f'\n***Deposit Successful => Current Balance: ${s.recv(1024).decode()}***\n')
        except ValueError:
            print("\n***Float & Character Values Are Not Allowed***\n")
        
        
        
    elif(Option == '2'):
        try:
            amountWithdraw = input("Enter The Amount You Would Like To Withdraw: ")
            while(int(amountWithdraw)<0 or amountWithdraw.isalpha()):
                print('\n***Amount Must Be Greater Than 0 And Float & Character Values Are Not Allowed***\n')
                amountWithdraw = input("Enter The Amount You Would Like To Withdraw: ")
            s.send(bytes(f'{Option} {amountWithdraw}', 'utf-8'))
            statusForAction = s.recv(1024).decode()
            if(statusForAction.split()[0] == '-1'):
                print(f'\n***Withdraw Amount ${amountWithdraw} Is Greater Than Current Balance ${statusForAction.split()[1]}***\n')
            else:
                print(f'\n***Withdraw Successful => Current Balance: ${statusForAction.split()[1]}***\n')
        except ValueError:
            print("\n***Float & Character Values Are Not Allowed***\n")

       
        
    elif(Option == '3'):
        s.send(bytes(f'{Option} {0}', 'utf-8'))
        currentBalance = s.recv(1024).decode()
        print(f'\n***Your Current Balance: ${currentBalance}***\n')
    
   

s.close()
