from socket import *
import socket
import threading
import logging
import time
import sys

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        buffer = ""
        while True:
            # receive data dari client dan decode data client menggunakan utf-8
            data = self.connection.recv(32).decode('utf-8')
            if data:
                buffer += data
                while "\r\n" in buffer:
                    command, buffer = buffer.split("\r\n", 1)
                    # menampilkan di terminal request yang dikirim client
                    logging.warning(f"[SERVER] menerima {command}")
                    # request TIME
                    if command == "TIME":
                        current_time = time.strftime("%H:%M:%S")
                        response = f"JAM {current_time}\r\n"
                        self.connection.sendall(response.encode('utf-8'))
                    # request quit
                    elif command == "QUIT":
                        self.connection.sendall("Keluar...\r\n".encode('utf-8'))
                        self.connection.close()
                        return
                    # request lainnya
                    else:
                        self.connection.sendall("Request tidak dikenal\r\n".encode('utf-8'))
            else:
                break
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # agar port sebelumnya bisa dipakai kembali
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        logging.warning("Server menyala dan open ke port 45000")
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"Koneksi dari {self.client_address}")
            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
    main()












