import http.server
import socketserver
import requests
import sqlite3
from bs4 import BeautifulSoup

conn = sqlite3.connect('laptops.db')
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())

PORT = 8000
Handler = MyHttpRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("Сервер запущен на порту", PORT)
httpd.serve_forever()
def get_html(url):
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    laptops = soup.find_all('div', class_='product_data__gtm-js')
    
    data = []
    for laptop in laptops:
        name = laptop.find('a', class_='link_gtm-js').text.strip()
        price = laptop.find('div', class_='product_price_final').text.strip()
        data.append((name, price))
    
    return data
def save_to_db(data):
    
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS laptops
                      (name TEXT, price TEXT)''')
    
    cursor.executemany('INSERT INTO laptops VALUES (?, ?)', data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    
    html = get_html(url)
    data = parse_page(html)
    save_to_db(data)

def searchfunc(query):
    answ = print_all()
    result = []
    for x in answ:
        if query.lower() in x[0].lower():
            result.append(x)
    return result

if __name__ == '__main__':
    app.run(debug=True)
