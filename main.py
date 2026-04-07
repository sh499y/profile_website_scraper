#!/usr/bin/env python
"""
MAIN FILE OF PROGRAM
Uruchamia spider'a Scrapy z interaktywnym inputem URL
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper_web.spiders.content import Content


def main():
    print("=" * 50)
    print("SCRAPER WEB - Web Scraping Tool")
    print("=" * 50)

    # Pobierz URL od użytkownika
    url = input("\nPodaj URL strony do scrapowania: ").strip()

    if not url:
        print("❌ Błąd: URL nie może być pusty!")
        return

    # Dodaj http:// jeśli brakuje
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
        print(f"ℹ️  Dodano https:// -> {url}")

    # Nazwa pliku output
    output_file = input("\nPodaj nazwę pliku output (domyślnie: output.json): ").strip()
    if not output_file:
        output_file = "output.json"

    if not output_file.endswith('.json'):
        output_file += '.json'

    print(f"\n🚀 Rozpoczynam scrapowanie...")
    print(f"   URL: {url}")
    print(f"   Output: {output_file}")
    print("-" * 50)

    # Konfiguracja Scrapy
    settings = get_project_settings()
    settings.set('FEEDS', {
        output_file: {
            'format': 'json',
            'encoding': 'utf-8',
            'overwrite': True
        }
    })

    # Uruchom spider'a
    process = CrawlerProcess(settings)
    process.crawl(Content, url=url)
    process.start()  # Blokujące - czeka na zakończenie

    print(f"\n✅ Zakończono! Wyniki zapisane w: {output_file}")


if __name__ == '__main__':
    main()