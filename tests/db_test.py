import sqlite3
conn = sqlite3.connect('automate.db')

c = conn.cursor()

c.execute('''CREATE TABLE add_buy
             (date text, buy_date text, symbol text, qty real, price real)''')

conn.close()