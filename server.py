# Davaleba 28:
import socket
import threading

def handle_client(client_socket, address, log_file):
    print(f"[+] New connection from {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
        
            with open(log_file, "a") as f:
                f.write(f"{address}: {message}\n")

            print(f"[{address}] {message}")
            client_socket.send(f"Received: {message}".encode("utf-8"))
    
        except ConnectionResetError:
            break

    print(f"[-] Connection closed from {address}")
    client_socket.close

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65142))
    server.listen(5)
    print("[*] Server started on 127.0.0.1:65432")

    log_file = 'chat_log.txt'

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, log_file))
        client_handler.start()
    
if __name__ == "__main__":
    main()