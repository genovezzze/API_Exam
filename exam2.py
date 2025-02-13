try:
    import requests
except ModuleNotFoundError:
    import os
    os.system('pip install requests')
    import requests

def get_countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    
    # 1. Pārbauda, vai pieprasījums bija veiksmīgs
    if response.status_code == 200:
        countries = response.json()
        print("API atbilde veiksmīgi saņemta!\n")
    else:
        print("Neizdevās iegūt datus. Statusa kods:", response.status_code)
        return
    
    # 2. Iegūst un izvada visu valstu vispārpieņemtos nosaukumus
    country_names = [country["name"]["common"] for country in countries]
    print("Visu valstu nosaukumi:")
    print(", ".join(country_names), "\n")
    
    # 3. Iegūst un izvada kopējo valstu skaitu
    total_countries = len(countries)
    print(f"Kopējais valstu skaits: {total_countries}\n")
    
    # 4. Iegūst un izvada vidējo iedzīvotāju skaitu
    total_population = sum(country.get("population", 0) for country in countries)
    avg_population = total_population / total_countries if total_countries else 0
    print(f"Vidējais iedzīvotāju skaits: {int(avg_population)}\n")
    
    # 5. Iegūst un izvada valsti ar vislielāko iedzīvotāju skaitu
    most_populated = max(countries, key=lambda c: c.get("population", 0))
    print(f"Vislielākā valsts pēc iedzīvotāju skaita: {most_populated['name']['common']} ({most_populated['population']})\n")
    
    # 6. Iegūst un izvada visu valstu kopējo platību
    total_area = sum(country.get("area", 0) for country in countries)
    print(f"Visu valstu kopējā platība: {total_area} km²\n")
    
    # 7. Iegūst un izvada informāciju par Latviju
    latvia = next((country for country in countries if country["name"]["common"] == "Latvia"), None)
    if latvia:
        subregion = latvia.get("subregion", "Nav datu")
        borders = ", ".join(latvia.get("borders", ["Nav robežvalstu"]))
        print(f"Latvijas apakšreģions: {subregion}")
        print(f"Latvijas robežvalstu kodi: {borders}")
    else:
        print("Latvija nav atrasta datu bāzē.")

# Izsauc funkciju
get_countries_data()
