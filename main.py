import requests
import sqlite3
from bs4 import BeautifulSoup

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
    conn = sqlite3.connect('laptops.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS laptops
                      (name TEXT, price TEXT)''')
    
    cursor.executemany('INSERT INTO laptops VALUES (?, ?)', data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    url = 'https://www.citilink.ru/catalog/igrovye-noutbuki/?pf=discount.any%2Crating.any&f=discount.any%2Crating.any%2C277_3ryzend15%2C277_3ryzend17%2C277_3ryzend19'
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
    parser(config.url)