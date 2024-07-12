from sqlalchemy import create_engine, Column, Integer, String, Float, Date, func, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# zakladni trida modelu
Base = declarative_base()
# definice modelu pro tabulku Uzivatel
class Uzivatel(Base):
    __tablename__ = 'uzivatele'
    id = Column(Integer, primary_key=True)
    jmeno = Column(String)
    email = Column(String)
    vek = Column(Integer)
 # vytvoreni connection stringu
connection_string = (
     'postgresql+psycopg2://koyeb-adm:b5lj0ipxmgsW@ep-patient-voice-a28tsil8.eu-central-1.pg.koyeb.app/sandbox?sslmode=require'
 )   
# vytvoreni engine
engine = create_engine(connection_string)
# vytvoreni session
Session = sessionmaker(bind=engine)
session = Session()
# vytvoreni tabulek
Base.metadata.create_all(engine)
# CREATE: Pridani noveho uzivatele
def pridat_uzivatele(jmeno, email, vek):
    novy_uzivatel = Uzivatel(jmeno=jmeno, email=email, vek=vek)
    session.add(novy_uzivatel)
    session.commit()
    print(f'Uzivatel {jmeno} pridan do databaze.')
# READ: Nacteni vsech uzivatelu
def nacti_uzivatele():
    uzivatele = session.query(Uzivatel).all()
    for uzivatel in uzivatele:
        print(f'ID: {uzivatel.id}, Jmeno: {uzivatel.jmeno}, Email: {uzivatel.email}, Vek: {uzivatel.vek}')
# UPDATE: Aktualizace uzivatele
def aktualizuj_uzivatele(id, nove_jmeno=None, novy_email=None, novy_vek=None):
    uzivatel = session.query(Uzivatel).filter_by(id=id).first()
    if uzivatel:
        if nove_jmeno:
            uzivatel.jmeno = nove_jmeno
        if novy_email:
            uzivatel.email = novy_email
        if novy_vek:
            uzivatel.vek = novy_vek
        session.commit()
        print(f'Uzivatel s ID {id} byl aktualizovan.')
    else:
        print(f'Uzivatel s ID {id} nebyl nalezen.')
# DELETE: Smazani uzivatele
def smazat_uzivatele(id):
    uzivatel = session.query(Uzivatel).filter_by(id=id).first()
    if uzivatel:
        session.delete(uzivatel)
        session.commit()
        print(f'Uzivatel s ID {id} byl smazan.')
    else:
        print(f'Uzivatel s ID {id} nebyl nalezen.')
# Priklad pouziti CRUD operaci
if __name__ == '__main__':
    # Pridani uzivatele
    pridat_uzivatele('Petr Kavan', 'petr.kavan@ekavan.com', 40)
    # Nacteni vsech uzivatelu
    nacti_uzivatele()
    # Aktualizace uzivatele
    aktualizuj_uzivatele(4, nove_jmeno='Jan Kahan', novy_email='jan.kahan@ekahan.com')
    # Nacteni vsech uzivatelu po aktualizaci
    nacti_uzivatele()
    # Smazani uzivatele
    smazat_uzivatele(1)
session.close()

