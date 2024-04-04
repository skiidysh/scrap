from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('laptops.db')
    cursor = conn.cursor()
    
    # Получаем данные из базы данных, сортируя ноутбуки по увеличению цены
    cursor.execute("SELECT * FROM laptops ORDER BY price")
    laptops = cursor.fetchall()
    
    conn.close()
    
    return render_template('index.html', laptops=laptops)

if __name__ == '__main__':
    app.run(debug=True)