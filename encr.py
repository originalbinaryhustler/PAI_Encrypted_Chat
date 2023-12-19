import socket
import threading 
import rsa
import time


public_key, private_key = rsa.newkeys(1024)
public_partner = None

def prnt_clr(text, color):
  if color == 'blue':
      print('\033[94m' + text + '\033[0m')
  elif color == 'red':
      print('\033[91m' + text + '\033[0m')
  elif color == 'green':
      print('\033[92m' + text + '\033[0m')
  elif color == 'yellow':
      print('\033[93m' + text + '\033[0m')
  elif color == 'light_purple':
      print('\033[94m' + text + '\033[0m')
  elif color == 'purple':
      print('\033[95m' + text + '\033[0m')
  elif color == 'cyan':
      print('\033[96m' + text + '\033[0m')
  elif color == 'light_gray':
      print('\033[97m' + text + '\033[0m')
  elif color == 'black':
      print('\033[98m' + text + '\033[0m')

prnt_clr('''
    
    
    
    
    
    
        
                                ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗    ╔═══╗╔══╗
                                ║╔═╗║║╔═╗║║╔══╝╚╗╔╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝
                                ║╚═╝║║╚═╝║║╚══╗ ║║║║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║    ║║ ║║ ║║ 
                                ║╔══╝║╔╗╔╝║╔══╝ ║║║║║╚═╝║  ║║  ║║ ║║║╔╗╔╝    ║╚═╝║ ║║ 
                                ║║   ║║║╚╗║╚══╗╔╝╚╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗    ║╔═╗║╔╣╠╗
                            lil ╚╝   ╚╝╚═╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝    ╚╝ ╚╝╚══╝






      ''', 'cyan')
time.sleep(2)
prnt_clr('''
         Do you want to host (1) or join a chat (2)?''', 'red')
time.sleep(.8)
choice = input('              >>>>  ')
prnt_clr('Enter the IP of the server: ', 'red')
IP = input('                  >>>>')
prnt_clr('Enter the port of the server: ', 'red')
PORT = int(input('            >>>>'))
if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    prnt_clr("Hosting has begun. Waiting for incoming connections...", 'yellow')

    
    client, _ = server.accept()
    client.send(public_key.save_pkcs1('PEM'))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024), 'PEM')
    prnt_clr("User has joined the chat.", 'blue')
elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP,PORT))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024), 'PEM')
    client.send(public_key.save_pkcs1('PEM'))
    prnt_clr("Joined the chat.", 'blue')
else:
    break
    
def sending_messages(c):
    while True:
        message = input('           >>>>')
        if message == 'exit()':
            break
        elif message == 'clear()':
            print('\n' * 100)
            continue
        elif message == 'help()':
            prnt_clr('exit() - exit the chat\nhelp() - show this message\nclear() - clear the screen', 'red')
            continue
        c.send(rsa.encrypt(message.encode(), public_partner))
       
        prnt_clr(f'\n📲🗯 You: ','purple')
        print(message)

def receiving_messages(c):
    while True:
        
        
        # print('\n📡🗯 Partner:' + rsa.decrypt(c.recv(1024), private_key).decode())
        decrypted_message = rsa.decrypt(c.recv(1024), private_key).decode()

# Print in green
        prnt_clr(f'\n📡🗯 Partner: ','green')
        print(decrypted_message)
        
threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()