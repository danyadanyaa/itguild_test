import socket
import threading
import logging
import sys

HOST = "127.0.0.1"
PORT = 12345

logging.basicConfig(
    filename="client.log", filemode="a", format="%(asctime)s - %(message)s", level=logging.INFO
)


def receive():
    while True:
        try:
            data = socket.recv(1024)
            print(data.decode())
        except Exception as e:
            logging.exception(e)
            socket.close()
            break


def send():
    while True:
        try:
            print("Write number for MarkoPolo\n")
            msg = input()
            if msg == 'quit':
                socket.send(msg.encode())
                print('Disconnected')
                raise Exception
            while not msg.isdigit():
                msg = input("Incorrect number, try again\n")
            msg_for_send = f'{msg}'
            socket.send(msg_for_send.encode())
        except Exception as e:
            logging.exception(e)
            socket.close()
            break


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((HOST, PORT))
    print(f'You connected to {HOST}:{PORT}. Type "quit" for disconnect')
except Exception as e:
    logging.exception(e)
    print(f'Server unavailable')
    sys.exit()

receive_thr = threading.Thread(target=receive)
send_thr = threading.Thread(target=send)

receive_thr.start()
send_thr.start()
