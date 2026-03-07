import json
import random

def generate_data(num_records=5000):
    imiona = ["Jan", "Anna", "Marek", "Katarzyna", "Piotr", "Małgorzata", "Tomasz", "Barbara", "Andrzej", "Magdalena", "Łukasz", "Agnieszka", "Michał", "Ewa", "Marcin", "Karolina", "Grzegorz", "Monika", "Paweł", "Joanna"]
    nazwiska = ["Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak", "Dąbrowski", "Kozłowski", "Mazur", "Jankowski", "Kwiatkowski", "Krawczyk"]
    
    data = []
    
    for _ in range(num_records):
        record = {
            "imie": random.choice(imiona),
            "nazwisko": random.choice(nazwiska),
            # Zakres do 8 lat (8 * 365 = 2920 dni)
            "dni_od_ostatniej_wizyty": random.randint(0, 2920),
            # Koordynaty wewnątrz granic Polski
            "lat": round(random.uniform(49.0, 54.8), 6),
            "lon": round(random.uniform(14.1, 24.1), 6)
        }
        data.append(record)
    
    with open('json_testowy_5000.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Pomyślnie wygenerowano plik z {num_records} rekordami.")

if __name__ == "__main__":
    generate_data(5000)