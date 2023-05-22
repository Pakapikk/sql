import sqlite3
import csv

conn = sqlite3.connect('epood_aratt.db')
c = conn.cursor()

# andmete lisamine
def lisa_andmed():
    nimi = input("Sisestage eesnimi: ")
    perenimi = input("Sisestage perenimi: ")
    email = input("Sisestage email: ")
    automark = input("Sisestage automark: ")
    mudel = input("Sisestage auto mudel: ")
    aasta = input("Sisestage aasta: ")
    hind = input("Sisestage hind: ")
    
    c.execute("INSERT INTO aratt (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (nimi, perenimi, email, automark, mudel, aasta, hind))
    conn.commit()
    print("Andmed on lisatud!")
    
# vanemad autod
def kuva_vanemad_autod():
    c.execute("SELECT * FROM aratt WHERE car_year < 2000 ORDER BY car_year ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
        
# keskmine
def keskmine_aasta_ja_kallim_hind():
    c.execute("SELECT AVG(car_year), MAX(car_price) FROM aratt")
    row = c.fetchone()
    print("Keskmine aasta:", row[0])
    print("Kõige kallim hind:", row[1])
    
# kõige uuema automargi kuvamiseks
def kuva_uuemad_automargid():
    c.execute("SELECT DISTINCT car_make, car_model FROM aratt ORDER BY car_year DESC LIMIT 5")
    rows = c.fetchall()
    for row in rows:
        print(row)
        
# kõige kallima automargi kuvamiseks perenime järgi
def kuva_kallimad_autod():
    automark = input("Sisestage automark: ")
    c.execute("SELECT * FROM aratt WHERE car_make = ? ORDER BY last_name DESC LIMIT 5",
              (automark,))
    rows = c.fetchall()
    for row in rows:
        print(row)
        
# andmete kustutamiseks ID järgi
def kustuta_andmed():
    id = input("Sisestage ID: ")
    c.execute("DELETE FROM aratt WHERE id = ?", (id,))
    conn.commit()
    print("Andmed on kustutatud!")
    
#kustutamine aasta ja automargi järgi
def kustuta_aasta_ja_automargi_jargi():
    aasta = input("Sisestage aasta: ")
    automark = input("Sisestage automark: ")
    c.execute("DELETE FROM aratt WHERE car_year < ? AND car_make = ?", (aasta, automark))
    conn.commit()
    print("Andmed on kustutatud!")

def ekspordi_andmed_csv_faili():
    conn = sqlite3.connect("epood_aratt.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aratt")
    rows = cursor.fetchall()

    with open('MOCK_DATA.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'first_name', 'last_name', 'email', 'car_make','car_model','car_year','car_price'])

        for row in rows:
            writer.writerow(row)

    print("Andmed on edukalt eksporditud CSV faili!")

    conn.commit()
    conn.close()
    
loop=1
while loop==1: 
    print("Autod")
    print("\nVali funktsioon:")
    print("1. Lisa andmed")
    print("2. Kuva vanemad autod")
    print("3. Kuva keskmine aasta ja kõige kallim hind")
    print("4. Kuva 5 kõige uuemat automarki kood mudeliga")
    print("5. Kuva 5 kõige kallimat sinu valitud automarki, sorteeri perenime järgi")
    print("6. Kustuta andmed ID järgi")
    print("7. Kustuta andmed aasta ja margi järgi")
    print("8. Ekspordi andmed CSV faili")
    print("9. Välju programmist")

    valik = input("Sisesta valiku number: ")

    if valik == "1":
        lisa_andmed()
    elif valik == "2":
        kuva_vanemad_autod()
    elif valik == "3":
        keskmine_aasta_ja_kallim_hind()
    elif valik == "4":
        kuva_uuemad_automargid()
    elif valik == "5":
        kuva_kallimad_autod()
    elif valik == "6":
        kustuta_andmed()
    elif valik == "7":
        kustuta_aasta_ja_automargi_jargi()
    elif valik == "8":
        ekspordi_andmed_csv_faili()
    elif valik == "9":
        break
    else:
        print("Vale valiku number, palun sisesta uuesti!")
