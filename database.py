import sqlite3

database = sqlite3.connect('silver.db')
cursor = database.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS categories(
#       category_id INTEGER PRIMARY KEY AUTOINCREMENT,
#      category_name TEXT UNIQUE )
#     ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS products(
#  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#  product_name TEXT UNIQUE,
# product_company TEXT,
# product_weight TEXT,
# product_silver TEXT,
#  product_price TEXT,
# product_description TEXT,
# category_id INTEGER ,
#  FOREIGN KEY(category_id) REFERENCES category(category_id)
#  )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS product_images(
#    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   product_id INTEGER,
#    product_image TEXT,
#   FOREIGN KEY(product_id) REFERENCES products(product_id)
#  )
#  ''')
# cursor.execute('''
#  CREATE TABLE IF NOT EXISTS product_videos(
#  video_id INTEGER PRIMARY KEY AUTOINCREMENT,
#  product_id INTEGER,
# product_text TEXT,
#   FOREIGN KEY(product_id) REFERENCES products(product_id)
#  )
# ''')

#
cursor.execute('''
 CREATE TABLE IF NOT EXISTS users(
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
telegram_id INTEGER UNIQUE,
 full_name TEXT,
contact TEXT)
 ''')
database.commit()
database.close()
