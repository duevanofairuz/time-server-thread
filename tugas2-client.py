import sys
import socket
import logging
import time



def kirim_data(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # logging.warning("membuka socket")
    # ip milik dan port yang mengarah ke mesin-1 (server)
    server_address = ('172.16.16.101', 45000)
    logging.warning(f"membuka socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        logging.warning(f"[CLIENT] mengirim {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        data = sock.recv(32)
        amount_received += len(data)
        logging.warning(f"[DITERIMA DARI SERVER] {data.decode('utf-8')}")
    finally:
        logging.warning("menutup socket")
        sock.close()
    return


if __name__=='__main__':
    kirim_data("TIME\r\n")
    # time.sleep(1)
    kirim_data("HALO\r\n")
    kirim_data("QUIT\r\n")
