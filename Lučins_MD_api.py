import requests

def get_universities_by_country(country):
    """Atgriež sarakstu ar augstskolām noteiktā valstī."""
    if not country:
        return []
    url = f"http://universities.hipolabs.com/search?country={country}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []

def count_universities(universities):
    """Atgriež augstskolu skaitu."""
    return len(universities)

def print_university_names(universities):
    """Izdrukā augstskolu nosaukumus."""
    for uni in universities:
        print(uni['name'])

def percentage_with_domain(universities, domain):
    """Aprēķina procentuālo daļu augstskolu, kuru mājas lapas adrese satur norādīto domēnu."""
    if not universities:
        return 0
    count = sum(1 for uni in universities if any(domain in url for url in uni.get('web_pages', [])))
    return round((count / len(universities)) * 100, 2)

def count_universities_with_name(universities, keyword):
    """Atgriež augstskolu skaitu, kuru nosaukumā ir noteikts vārds."""
    return sum(1 for uni in universities if keyword.lower() in uni['name'].lower())

def get_university_count_by_country():
    """Atgriež vārdnīcu ar valstu nosaukumiem un to augstskolu skaitu."""
    url = "http://universities.hipolabs.com/search"
    try:
        response = requests.get(url)
        response.raise_for_status()
        universities = response.json()
    except requests.RequestException:
        return {}

    country_count = {}
    for uni in universities:
        country = uni.get('country', 'Unknown')
        country_count[country] = country_count.get(country, 0) + 1
    return country_count

latvia_universities = get_universities_by_country("Latvia")
print(f"Latvijā ir {count_universities(latvia_universities)} augstskolas")
print_university_names(latvia_universities)

france_universities = get_universities_by_country("France")
print(f"Francijā ir {count_universities(france_universities)} augstskolas")

percentage_eu = percentage_with_domain(france_universities, ".eu")
print(f"Francijas augstskolām {percentage_eu}% ir mājas lapa ar .eu domēnu")

paris_count = count_universities_with_name(france_universities, "Paris")
print(f"Francijā {paris_count} augstskolu nosaukumā ir vārds 'Paris'")

count_school = count_universities_with_name(universities_worldwide, "School")
print(f"Pasaulē ir {count_school} augstskolas, kuru nosaukumā ir vārds 'School'")

percentage_https = percentage_with_domain(france_universities, "https")
print(f"Francijā {percentage_https}% augstskolu mājas lapas izmanto HTTPS")

country_university_count = get_university_count_by_country()
if country_university_count:
    most_universities_country = max(country_university_count, key=country_university_count.get, default="Unknown")
    print(f"Eiropas valsts ar visvairāk augstskolām ir {most_universities_country} ({country_university_count.get(most_universities_country, 0)} augstskolas)")
else:
    print("Neizdevās iegūt datus par augstskolu skaitu pasaulē.")
