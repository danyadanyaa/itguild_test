import logging
import socket
import threading
from service import markopolo

HOST = "127.0.0.1"
PORT = 12345

clients = set()

logging.basicConfig(
    filename="server.log", filemode="a", format="%(asctime)s - %(message)s", level=logging.INFO
)


def new_client(connection: socket.socket, user_ip, user_port) -> None:
    with connection:
        while True:
            try:
                data = connection.recv(1024)
                data_str = data.decode()
                if data.decode() == 'quit':
                    raise Exception(f"{user_ip}:{user_port} is disconnected")
                print(f"Received {data}, от {user_ip}:{user_port}")
                logging.info(f"{user_ip}:{user_port}//{data}") if data else None
                result = markopolo(int(data_str))
                connection.send(str(result).encode())
            except Exception as e:
                logging.exception(e)
                clients.remove(connection)
                print(f"{user_ip}:{user_port} is disconnected")
                break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        user_ip, user_port = addr
        clients.add(conn)
        print(f"{user_ip}:{user_port} is connected")
        thr = threading.Thread(target=new_client, args=(conn, user_ip, user_port))
        thr.start()
