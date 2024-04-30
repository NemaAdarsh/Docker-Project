import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import socket

def scrape_articles(target_url):
    req = requests.get(target_url)
    soup = BeautifulSoup(req.content , "html.parser")
    text = soup.get_text()
    count = len(text.split())

    data = {
        'target link': [target_url],
        'scraped data': [text],
        'count of words': [count]
    }

    df = pd.DataFrame(data)
    return df

def save_to_csv(data, filename="shared-data/scraped_articles.csv"):
    data.to_csv(filename, index=False)

def get_data(link, filename="shared-data/scraped_articles.csv"):
    df = pd.read_csv(filename)
    link_data = df[df['target link'] == link]
    count = link_data.iloc[0]['count of words']
    return count

def establish_socket_connection():
    host = '0.0.0.0'  
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server listening on port:", port)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Received URL:", data)
                scraped_data = scrape_articles(data)
                save_to_csv(scraped_data)
                conn.sendall(b'Data scraped and saved to scraped_articles.csv')
                break

if __name__ == "__main__":
    establish_socket_connection()
