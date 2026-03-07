# 🗺️ Planer Wizyt Terenowych (Polska)
**Wersja 1.9 | Autor: Jan Kłomski 2026**

Lekka i szybka aplikacja webowa do wizualizacji bazy klientów na mapie Polski. Stworzona, aby ułatwić planowanie tras i identyfikację miejsc, które wymagają ponownej wizyty.

---

## 🚀 Szybki Start

1. **Przygotuj dane**: Wyeksportuj tabelę z bazy MS Access.
2. **Konwersja**: Jeśli masz plik XML, użyj linku w ustawieniach aplikacji, aby zamienić go na format **JSON**.
3. **Wczytanie**: Kliknij przycisk `+` (Dodaj) i wybierz plik `.json`.
4. **Zarządzanie**: Otwórz `Ustawienia` (ikonka suwaków), aby dostosować przedziały czasowe i kolory.

---

## 🛠️ Kluczowe Funkcjonalności

* **Dynamiczne Kolorowanie**: Znaczniki zmieniają kolor w zależności od liczby dni od ostatniej wizyty (np. Zielony -> Żółty -> Czerwony).
* **Inteligentne Filtrowanie**: Możliwość ukrycia "świeżych" wizyt i skupienia się wyłącznie na punktach krytycznych (np. powyżej roku bez odwiedzin).
* **Interaktywne Narzędzia**:
    * **Nawigacja**: Jedno kliknięcie w punkcie otwiera trasę w aplikacji Google Maps.
    * **Połączenia**: Jeśli baza zawiera numer telefonu, możesz zadzwonić do klienta bezpośrednio z mapy.
    * **Licznik**: Bieżąca informacja o liczbie wyświetlonych punktów po nałożeniu filtrów.
* **Optymalizacja Mobile**: Duże przyciski i responsywny interfejs ułatwiają obsługę na smartfonie w samochodzie.

---

## 📊 Format Danych (JSON)

Aplikacja przyjmuje pliki w formacie JSON. Każdy rekord powinien wyglądać następująco:

```json
{
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "dni_od_ostatniej_wizyty": 450,
    "lat": 52.2297,
    "lon": 21.0122,
    "tel": "123456789"
}

```
---

## Narzędzia testowe
Zostawiam do testu przykładowe wygenerowane pliki do testowania z 2000 rekordów i 5000 rekordów. Znajdują sie one w folderze /Testing.

---
Jan Kłomski 2026
