import requests
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

countries = response.json()
visi_valsti = len(countries)
print(f"Informācija pieejama par {visi_valsti} valstīm")
un_member_countries = sum(1 for country in countries if 'unMember' in country and country['unMember'])
print(f"Apvienoto Nāciju Organizācijā ir {un_member_countries} valstis")
pirmdiena_sakums = sum(1 for country in countries if 'startOfWeek' in country and country['startOfWeek'] == 'monday')
pirmdiena = (pirmdiena_sakums / visi_valsti) * 100
print(f"{pirmdiena:.2f}% valstīs diena sākas ar pirmdienu")
republika = sum(1 for country in countries if 'name' in country and 'common' in country['name'] and 'Republic' in country['name']['common'])
print(f"Oficiālajos nosaukumos angļu valodā Republic ir {republika} valstīs")

koordinates = [57.801558744803096, 23.240355694350477]
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
tuvakais_valsts = None
min_distancija = float('inf')
for country in countries:
    if 'latlng' in country:
        lat, lon = country['latlng'][0], country['latlng'][1]
        dist = distance(koordinates, [lat, lon])
        if dist < min_distancija:
            min_distancija = dist
            tuvakais_valsts = country['name']['common']
print(f"Valsts, kas atrodas vistuvāk norādītajiem koordinātēm, ir {tuvakais_valsts}")

eiropas_p = 0
eiropas_v = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia',
    'Finland', 'Georgia', 'Germany', 'Hungary', 'Iceland', 'Ireland', 'Kazakhstan', 'Kosovo',
    'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
    'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino',
    'Serbia', 'Slovakia', 'Slovenia', 'Switzerland', 'Turkey', 'Ukraine'
]
for country in countries:
    if 'region' in country and country['region'] == 'Europe' and 'borders' in country and len(country['borders']) > 0:
        if country['name']['common'] in eiropas_v:
            if 'population' in country:
                eiropas_p += country['population']
print(f"Kopējais iedzivotāju skaits Eiropas sauszemes robežas valstīs ir {eiropas_p}")

