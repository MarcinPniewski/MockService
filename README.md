# MockService

## Opis

Jest to zaślepka hipotetycznej aplikacji testowej, napisana w Flasku.

Symuluje odpowiedzi zwracane przez hipotetyczny serwis, obsługując metodę HTTP `GET` na ścieżce: `GET /status_zadania?kod=<nazwa_zadania>`.

Działanie zależy od przesłanego parametru `kod`:

| kod                  | Status HTTP | Źródło odpowiedzi        | Uwagi                                                                          |
|----------------------|-------------|--------------------------|--------------------------------------------------------------------------------|
| `zadanie_1`          | 200         | `responses/zadanie_1.*`  | Plik z surową odpowiedzią ('txt', 'html', 'xml', 'json')                       |
| `zadanie_2`          | 200         | `responses/zadanie_2.*`  | Plik z surową odpowiedzią ('txt', 'html', 'xml', 'json')                       |
| `zadanie_3` lub inne | 400         | `responses/nieznane.*`   | W treści pliku podmieniany jest fragment `?kod=zadanie_3` na rzeczywisty `kod` |
| (brak parametru)     | 400         | —                        | Zwracana treść: `Brak parametru 'kod'`                                         |

Obsługiwane są różne formaty odpowiedzi (np. `.txt`, `.html`, `.xml`, `.json`) z automatycznym ustawianiem nagłówka `Content-Type`.


## Struktura projektu

- `app/__init__.py` – funkcja create_app() inicjalizująca aplikację Flask
- `app/routes.py` – definicja tras HTTP oraz logika odpowiedzi
- `app/logger.py` – konfiguracja logowania (ścieżki, format, poziom logów)
- `app/responses/` – katalog z odpowiedziami dla testów API (obsługiwane różne rozszerzenia)
- `run.py` – główny plik uruchamiający aplikację (flask run, python run.py)

## Wymagania

- Python 3.8+
- Flask 2.x

## Uruchomienie

```bash
pip3 install --no-cache-dir -r requirements.txt
python run.py
```

## Licencja

To repozytorium udostępniane jest wyłącznie do celów testowych i edukacyjnych.  
Wszelkie inne formy użycia (modyfikacja, komercja, publikacja) są zabronione.  
Szczegóły w pliku [LICENSE.txt](./LICENSE.txt).