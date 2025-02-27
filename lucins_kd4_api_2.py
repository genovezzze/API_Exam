import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

if response.status_code != 200:
    print("Kļūda, nesaņemot datus no API.")
    exit()

countries = response.json()

total_countries = len(countries)
print(f"Informācija pieejama par {total_countries} valstīm.")
un_member_countries = sum(1 for country in countries if 'unMember' in country and country['unMember'])
print(f"Apvienoto Nāciju Organizācijā ir {un_member_countries} valstis.")
monday_start_count = sum(1 for country in countries if 'startOfWeek' in country and country['startOfWeek'] == 'monday')
monday_percentage = (monday_start_count / total_countries) * 100
print(f"{monday_percentage:.2f}% valstīs diena sākas ar pirmdienu.")
republic_count = sum(1 for country in countries if 'name' in country and 'common' in country['name'] and 'Republic' in country['name']['common'])
print(f"Oficiālajos nosaukumos angļu valodā 'Republic' ir {republic_count} valstīs.")

target_coordinates = [57.801558744803096, 23.240355694350477]
def distance(coord1, coord2):
    from math import radians, sin, cos, sqrt, atan2
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    R = 6371  
    distance = R * c
    return distance
closest_country = None
min_distance = float('inf')
for country in countries:
    if 'latlng' in country:
        lat, lon = country['latlng'][0], country['latlng'][1]
        dist = distance(target_coordinates, [lat, lon])
        if dist < min_distance:
            min_distance = dist
            closest_country = country['name']['common']
print(f"Valsts, kas atrodas vistuvāk norādītajiem koordinātēm, ir {closest_country}.")

europe_landlocked_population = 0
landlocked_european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia',
    'Finland', 'Georgia', 'Germany', 'Hungary', 'Iceland', 'Ireland', 'Kazakhstan', 'Kosovo',
    'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
    'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino',
    'Serbia', 'Slovakia', 'Slovenia', 'Switzerland', 'Turkey', 'Ukraine'
]
for country in countries:
    if 'region' in country and country['region'] == 'Europe' and 'borders' in country and len(country['borders']) > 0:
        if country['name']['common'] in landlocked_european_countries:
            if 'population' in country:
                europe_landlocked_population += country['population']
print(f"Kopējais iedzīvotāju skaits Eiropas sauszemes robežas valstīs ir {europe_landlocked_population}.")

