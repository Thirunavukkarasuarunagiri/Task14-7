import requests

class OpenBreweryDB:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def get_breweries_by_state(self, state):
        response = requests.get(f"{self.base_url}?by_state={state}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data for {state}.")
            return []

    def list_breweries_names(self, breweries):
        names = [brewery['name'] for brewery in breweries]
        return names

    def count_breweries_by_state(self, state):
        breweries = self.get_breweries_by_state(state)
        count = len(breweries)
        return count

    def count_brewery_types_by_city(self, state):
        breweries = self.get_breweries_by_state(state)
        types_count_by_city = {}
        for brewery in breweries:
            city = brewery['city']
            brewery_type = brewery['brewery_type']
            if city not in types_count_by_city:
                types_count_by_city[city] = {}
            types_count_by_city[city][brewery_type] = types_count_by_city[city].get(brewery_type, 0) + 1
        return types_count_by_city

    def count_breweries_with_website(self, state):
        breweries = self.get_breweries_by_state(state)
        count_with_website = sum(1 for brewery in breweries if 'website_url' in brewery and brewery['website_url'])
        return count_with_website

openbrewerydb = OpenBreweryDB()

# 1. List the names of all breweries present in the states of Alaska, Maine, and New York
states = ["Alaska", "Maine", "New York"]
for state in states:
    breweries = openbrewerydb.get_breweries_by_state(state)
    brewery_names = openbrewerydb.list_breweries_names(breweries)
    print(f"\nBreweries in {state}:")
    for name in brewery_names:
        print(name)

# 2. Count of breweries in each of the states mentioned above
print("\nCount of breweries in each state:")
for state in states:
    count = openbrewerydb.count_breweries_by_state(state)
    print(f"{state}: {count}")

# 3. Count the number of types of breweries present in individual cities of the states mentioned above
print("\nCount of brewery types by city:")
for state in states:
    types_count_by_city = openbrewerydb.count_brewery_types_by_city(state)
    print(f"\n{state}:")
    for city, types_count in types_count_by_city.items():
        print(f"{city}: {types_count}")

# 4. Count and list how many breweries have websites in the states of Alaska, Maine, and New York
print("\nCount of breweries with websites:")
for state in states:
    count_with_website = openbrewerydb.count_breweries_with_website(state)
    print(f"{state}: {count_with_website}")