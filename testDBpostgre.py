import psycopg2
from psycopg2 import sql

# Přihlašovací údaje k databázi
db_params = {
    'dbname': 'koyebdb',
    'user': 'koyeb-adm',
    'password': 'b5lj0ipxmgsW',
    'host': 'ep-patient-voice-a28tsil8.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}

# Připojte se k PostgreSQL serveru
conn = psycopg2.connect(**db_params)
conn.autocommit = True
cursor = conn.cursor()

# Vytvořte tabulky
create_tables_query = '''
CREATE TABLE IF NOT EXISTS goods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    cost_price NUMERIC(10, 2) NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    sale_price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    position VARCHAR(50) NOT NULL,
    date_of_employment DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20),
    gender VARCHAR(10),
    order_history TEXT,
    discount_percentage NUMERIC(5, 2),
    registration_date DATE NOT NULL,
    subscribed_to_mailing BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    goods_id INT REFERENCES goods(id),
    sale_price NUMERIC(10, 2) NOT NULL,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    employee_id INT REFERENCES employees(id),
    client_id INT REFERENCES clients(id)
);
'''

cursor.execute(create_tables_query)

# Potvrďte změny a uzavřete připojení
conn.commit()
cursor.close()
conn.close()

print("Tabulky byly úspěšně vytvořeny v databázi 'koyebdb'.")
