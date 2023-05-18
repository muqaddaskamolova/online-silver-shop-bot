import sqlite3


def insert_category(category_name):
    database = sqlite3.connect('silver.db')
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO categories(category_name)
    VALUES (?)
    ''', (category_name,))

    database.commit()
    database.close()


def insert_user(telegram_id, full_name, contact):
    database = sqlite3.connect('silver.db')
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO users(telegram_id, full_name, contact)
    VALUES (?, ?, ?)
    ''', (telegram_id, full_name, contact))

    database.commit()
    database.close()


def insert_product(name, company, weight, silver, price, description, category):
    database = sqlite3.connect('silver.db')
    cursor = database.cursor()

    cursor.execute('''INSERT INTO products(product_name,
     product_company, 
     product_weight,
     product_silver, 
     product_price,
     product_description, 
     product_category) 

    VALUES (?, ?, ?, ?, ?,?, ?, )
    ''', (name, company, weight, silver, price, description, category))

    database.commit()
    database.close()
