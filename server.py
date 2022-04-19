# Name: Gurnaman Singh
# ID: 010851677 

from base64 import encode
import socket
s = socket.socket()
print('Socket created successfully')
port = 56789
s.bind(('', port))
print(f'socket binded to port {port}')
s.listen(5)

currentBalance = 100

print('Socket is listening')

c, addr = s.accept()
print('Got connection from ', addr)
message =  'Thank You For Connecting'
c.send(bytes(f'{message}', 'utf-8'))

while True:
   

    stringReceived = c.recv(1024).decode()
    stringReceivedSplitVersion = stringReceived.split()
    Option = stringReceivedSplitVersion[0]
    amountDeposit = int(stringReceivedSplitVersion[1])
    amountWithdraw = int(stringReceivedSplitVersion[1])
    print(f'Option Selected {Option}')
    if(Option == '0'):
        c.close()
        break
    elif(Option == '1'):
        currentBalance += amountDeposit
        c.send(bytes(f'{currentBalance}', 'utf-8'))
    elif(Option == '2'):
        if(currentBalance>=amountWithdraw):
            currentBalance -= amountWithdraw
            c.send(bytes(f'1 {currentBalance}', 'utf-8'))
        else:
            c.send(bytes(f'-1 {currentBalance}', 'utf-8'))
    elif(Option == '3'):
        c.send(bytes(f'{currentBalance}', 'utf-8')) 
    