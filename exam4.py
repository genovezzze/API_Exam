import requests
# Importē requests bibliotēku, lai veiktu HTTP pieprasījumus
def get_waste_sorting_points():
    # Funkcija, kas iegūst un apstrādā atkritumu šķirošanas punktus
    url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d"
    # API URL, no kura tiek iegūti dati
    try:
        response = requests.get(url)  # Veic GET pieprasījumu uz norādīto URL
        if response.status_code != 200:
            # Ja atbilde nav veiksmīga, izvada kļūdas ziņojumu un beidz funkciju
            print("Serveris neatbild vai atbild ar kļūdu.")
            return
        data = response.json()  # Pārveido saņemto JSON atbildi par Python vārdnīcu
        if not data.get("result", {}).get("records", []):
            # Ja serveris atgriež tukšu datu kopu, izvada attiecīgu paziņojumu
            print("Serveris atbildēja ar tukšu datu kopu.")
            return
        records = data["result"]["records"]  # Iegūst ierakstu sarakstu no atbildes
        for record in records:
            # Iterē cauri katram ierakstam un pārbauda, vai tas satur nepieciešamos atkritumu veidus
            address = record.get("Adrese", "Nav norādīts")  # Iegūst adresi, ja tā ir norādīta
            region = record.get("Novads", "Nav norādīts")  # Iegūst novada nosaukumu
            if record.get("8 : Baterijas un akumulatori") == "x":
                # Ja var nodot baterijas un akumulatorus, izvada informāciju
                print(f"Baterijas un akumulatorus var nodot: {address}, {region}")
            if record.get("10 : Nolietotās riepas") == "x":
                # Ja var nodot nolietotās riepas, izvada informāciju
                print(f"Nolietotās riepas var nodot: {address}, {region}")
            if record.get("3 : Metāls") == "x":
                # Ja var nodot metālu, izvada informāciju
                print(f"Metālu var nodot: {address}, {region}")
    except requests.exceptions.RequestException:
        # Ja pieprasījums neizdodas, izvada kļūdas ziņojumu
        print("Nevar izveidot savienojumu ar serveri.")

get_waste_sorting_points()  # Izsauc funkciju, lai iegūtu un apstrādātu datus
