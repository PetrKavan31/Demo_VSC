import psycopg2
from psycopg2 import sql

# Přihlašovací údaje k databázi
sandbox = {
    'dbname': 'sandbox',
    'user': 'koyeb-adm',
    'password': 'b5lj0ipxmgsW',
    'host': 'ep-patient-voice-a28tsil8.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}

#1. vytvoreni pripojeni
conn = psycopg2.connect(**sandbox)
#2. Vytvoření kurzoru
cur = conn.cursor()
#3. SQL prikaz!
cur.execute('''
    CREATE TABLE IF NOT EXISTS lidi (
        name VARCHAR(100),
        age INTEGER
    )
''')
#4. Uložení změn
conn.commit()
#5. Uzavření kurzoru
cur.close()
#6. Uzavreni spojení
conn.close()

print("Tabulky byly úspěšně vytvořeny v databázi 'sandbox'.")