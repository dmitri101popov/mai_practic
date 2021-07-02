from os import name
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1235))

users = []

server.listen(5)
print("Server start listening")
print("---------------chat history-----------------")

def send_all(message, ignore):
    for user in users:
        print(user)
        if ignore != user:
            user.send(message)

def listen_user(user):
    while True:
        message = user.recv(2048)
        print(f"User sent: {message.decode('utf-8')}")

        send_all(message, user)




def start():
    while True:
        user_socket, adress = server.accept()
        print(f"user{adress[0]} connected to server")
        users.append(user_socket)

        new_user_listen = threading.Thread(target=listen_user, args=(user_socket,))
        
        new_user_listen.start()


if __name__ == '__main__':
    start()