## web_scraper.py
import requests
from bs4 import BeautifulSoup
from typing import Dict

class WebScraper:
    def scrape_for_currencies(self, url: str = "https://example.com") -> Dict[str, float]:
        """
        Scrape the given URL for currency information.
        
        :param url: The URL to scrape for currency data.
        :return: A dictionary containing currency information.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to {url}: {e}")

        soup = BeautifulSoup(response.content, 'html.parser')
        currencies_info = {}

        # Assuming the webpage has a list of currencies in a table with 'currency-name' and 'currency-value' class names
        for row in soup.find_all('tr'):
            name_data = row.find('td', class_='currency-name')
            value_data = row.find('td', class_='currency-value')
            if name_data and value_data:
                try:
                    currency_name = name_data.text.strip()
                    currency_value = float(value_data.text.strip())
                    currencies_info[currency_name] = currency_value
                except ValueError:
                    continue  # Skip rows with invalid data

        return currencies_info
