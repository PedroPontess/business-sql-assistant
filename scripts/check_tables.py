import sqlite3

# Conectar à base de dados
conn = sqlite3.connect('Chinook.db')
cursor = conn.cursor()

# Pedir lista de todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("--- TABELAS ENCONTRADAS ---")
for table in tables:
    print(table[0])
    
conn.close()