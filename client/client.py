import socket

def send_url_to_server(url):
    host = 'server-container'  
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(url.encode())
        data = s.recv(1024)
        print(data.decode())

if __name__ == "__main__":
    url = input("Enter the URL: ")
    send_url_to_server(url)
