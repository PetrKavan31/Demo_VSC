import psycopg2

class PostgreSQLDatabase:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.sslmode = 'require'

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            dbname=self.database,
            sslmode = self.sslmode
        )
        self.cursor = self.connection.cursor()
        print("Připojeno k databázi.")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Odpojeno od databáze.")

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        print("Dotaz byl úspěšně proveden.")

#Volani
# Přihlašovací údaje k databázi
host = 'ep-patient-voice-a28tsil8.eu-central-1.pg.koyeb.app'  # Např. 'localhost'
port = '5432'
username = 'koyeb-adm'  # Vaše uživatelské jméno
password = 'b5lj0ipxmgsW'  # Vaše heslo
database = 'koyebdb'  # Název vaší databáze

# Inicializace připojení k databázi
db = PostgreSQLDatabase(host, port, username, password, database)
db.connect()

# Vytvoření tabulek
create_tables_query = '''
    CREATE TABLE IF NOT EXISTS test1 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
'''

db.execute_query(create_tables_query)

# Odpojení od databáze
db.disconnect()

print("Tabulky byly úspěšně vytvořeny v databázi 'testDB'.")

