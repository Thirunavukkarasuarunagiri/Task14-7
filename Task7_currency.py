import requests

class CountryDataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the provided URL")
            return None

    def display_country_info(self, data):
        print("Countries Info:")
        for country in data:
            name = country.get("name", "N/A")
            currencies = country.get("currencies", [])
            if currencies:
                currency_name = currencies[0].get("name", "N/A")
                currency_symbol = currencies[0].get("symbol", "N/A")
                print(f"Name: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def display_dollar_countries(self, data):
        print("\nCountries with Dollar currency:")
        for country in data:
            currencies = country.get("currencies", [])
            for currency in currencies:
                if currency.get("name") == "United States dollar":
                    print(country.get("name"))
                    break

    def display_euro_countries(self, data):
        print("\nCountries with Euro currency:")
        for country in data:
            currencies = country.get("currencies", [])
            for currency in currencies:
                if currency.get("name") == "Euro":
                    print(country.get("name"))
                    break

# Instantiate the CountryDataFetcher class with the provided URL
url = "https://restcountries.com//v3.1/all"
data_fetcher = CountryDataFetcher(url)

# Fetch data
data = data_fetcher.fetch_data()

if data:
    # Display country info
    data_fetcher.display_country_info(data)

    # Display countries with Dollar currency
    data_fetcher.display_dollar_countries(data)

    # Display countries with Euro currency
    data_fetcher.display_euro_countries(data)