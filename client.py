import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 65142))

    print("[*] Connected to server. Type your message below.")

    try:
        while True:
            message = input("> ")
            if message.lower() == "exit":
                break

            client.send(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(response)

    except KeyboardInterrupt:
        print("\n[!] Exiting chat.")
    
    client.close()

if __name__ == "__main__":
    main()