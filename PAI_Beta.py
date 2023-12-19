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
prnt_clr('\n Enter the IP of the server: ', 'red')
IP = input('                  >>>>')
prnt_clr('\n Enter the port of the server: ', 'red')
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
    pass
 
 
 
 
 
 
def encode_txt(text):
   # Create a dictionary that maps each character to its ASCII value
   encoding_dict = {chr(i): chr((i + 10) % 256) for i in range(256)}
   # Encode the text
   encoded_text = ''.join(encoding_dict[char] for char in text)
   return encoded_text

def decode(encoded_text):
   # Create a dictionary that maps each character to its ASCII value
   decoding_dict = {chr((i + 10) % 256): chr(i) for i in range(256)}
   # Decode the text
   decoded_text = ''.join(decoding_dict[char] for char in encoded_text)
   return decoded_text

import math

def encode(ip, port):
  # Split the IP address into octets
  ip_octets = ip.split('.')
  # Convert each octet to an integer, take the square root, and then multiply by a constant
  encoded_ip = '.'.join(str(math.sqrt(int(octet)) * 10) for octet in ip_octets)
  # Take the square root of the port, and then multiply by a constant
  encoded_port = math.sqrt(port) * 1000
  return encoded_ip, encoded_port

def decode(encoded_ip, encoded_port):
  # Split the encoded IP address into octets
  ip_octets = encoded_ip.split('.')
  # Convert each octet to an integer, divide by a constant, and then square
  decoded_ip = '.'.join(str((int(octet) / 10) ** 2) for octet in ip_octets)
  # Divide the encoded port by a constant, and then square
  decoded_port = (encoded_port / 1000) ** 2
  return decoded_ip, decoded_port

 
def encode():
    ip_to_scramble = input('Input IP Address to encode')
    port_to_scramble = input('Input Port to encode')
    return prnt_clr('''
    Encoded IP = {ip_to_scramble}
    Encoded Port = {port_to_scramble}
                 ''', 'yellow')
def decode():
    ip_to_unscramble = input('Input IP Address to encode')
    port_to_unscramble = input('Input Port to encode')
    return prnt_clr('''
    Dencoded IP = {ip_to_scramble}
    Dencoded Port = {port_to_scramble}
                 ''', 'yellow')
    
    
    
    
    
    
    
    
    
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