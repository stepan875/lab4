from models import get_db_connection, init_db

def seed_products():
    init_db() 
    conn = get_db_connection()
    products = [
        ('Ноутбук Lenovo IdeaPad 3', 18000.00, '/api/placeholder/200/200'),
        ('Монітор Samsung 24"', 7200.00, '/api/placeholder/200/200'),
        ('Мишка Logitech MX Master', 2600.00, '/api/placeholder/200/200'),
        ('Клавіатура Razer BlackWidow', 3200.00, '/api/placeholder/200/200'),
        ('Гарнітура HyperX Cloud II', 4500.00, '/api/placeholder/200/200'),
        ('Системний блок HP Pavilion', 30000.00, '/api/placeholder/200/200'),
        ('Планшет iPad Air', 24000.00, '/api/placeholder/200/200'),
        ('Принтер Canon PIXMA', 5200.00, '/api/placeholder/200/200'),
        ('Зовнішній жорсткий диск WD 2TB', 3500.00, '/api/placeholder/200/200'),
        ('Флешка SanDisk 64GB', 400.00, '/api/placeholder/200/200')
    ]
    
    conn.executemany('INSERT INTO products (name, price, image) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_products()
    print("Тестові продукти додано до бази даних.")