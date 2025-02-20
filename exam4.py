import requests
def get_waste_sorting_points():
    url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Serveris neatbild vai atbild ar kļūdu.")
            return
        data = response.json()
        if not data.get("result", {}).get("records", []):
            print("Serveris atbildēja ar tukšu datu kopu.")
            return
        records = data["result"]["records"]
        for record in records:
            address = record.get("Adrese", "Nav norādīts")
            region = record.get("Novads", "Nav norādīts")
            if record.get("8 : Baterijas un akumulatori") == "x":
                print(f"Baterijas un akumulatorus var nodot: {address}, {region}")
            if record.get("10 : Nolietotās riepas") == "x":
                print(f"Nolietotās riepas var nodot: {address}, {region}")
            if record.get("3 : Metāls") == "x":
                print(f"Metālu var nodot: {address}, {region}")
    except requests.exceptions.RequestException:
        print("Nevar izveidot savienojumu ar serveri.")
get_waste_sorting_points()
