
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1235))
print("----------------------App started-------------------------")

def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode("utf-8"))

def send_to_server():
    listen_thread = threading.Thread(target=listen_server)
    listen_thread.start()

    while True:
        client.send(input("You: ").encode('utf-8'))


if __name__ == "__main__":
    send_to_server()
