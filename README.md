# Scraper Web

Projekt Scrapy do web scrapingu.

## Instalacja

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# lub
.venv\Scripts\activate  # Windows

pip install scrapy
```

## Uruchomienie

```bash
# Lista dostępnych spider'ów
scrapy list

# Uruchomienie spider'a
scrapy crawl cytaty_spider

# Zapis do pliku
scrapy crawl cytaty_spider -o output.json
scrapy crawl cytaty_spider -o output.csv
```

## Struktura projektu

```
scraper_web/
├── scrapy.cfg              # Konfiguracja Scrapy
├── scraper_web/
│   ├── __init__.py
│   ├── items.py           # Definicje items
│   ├── middlewares.py     # Custom middlewares
│   ├── pipelines.py       # Data pipelines
│   ├── settings.py        # Ustawienia projektu
│   └── spiders/           # Spider'y
│       ├── __init__.py
│       └── cytaty_spider.py
```

## Tworzenie nowego spider'a

```bash
scrapy genspider nazwa_spider example.com
```
## Korzystanie z programu
```
scrapy crawl content -a url=https://quotes.toscrape.com/page/2/
```