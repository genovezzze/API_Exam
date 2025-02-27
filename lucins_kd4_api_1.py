import pandas as pd

data = pd.read_csv("pokemon_data.csv")
data.columns = data.columns.str.strip()
print("Pieejamās kolonnas:", data.columns)

best_attack = data.loc[data['Attack'].idxmax()]
print(f"Visaugstākais uzbrukuma rādītājs ir Pokémonam {best_attack['Name']} ar uzbrukuma rādītāju {best_attack['Attack']}.")
if 'HP' in data.columns:
    videjais_hp = data['HP'].mean()
    print(f"Vidējais HP rādītājs visā datu kopā ir {videjais_hp:.2f}.")
if 'Type 1' in data.columns:
    water = data[data['Type 1'] == 'Water'].shape[0]
    print(f"Ūdens tipa pokemoni: {water}.")
if 'Speed' in data.columns:
    speed = data.loc[data['Speed'].idxmax()]
    print(f"Vislielākais ātrums ir Pokémonam {speed['Name']} ar ātrumu {speed['Speed']}.")
if 'Type 1' in data.columns:
    parastie = data['Type 1'].mode()[0]
    print(f"Visbiežāk sastopamais Pokémonu tips ir {parstie}.")
if 'Defense' in data.columns:
    defense = data.loc[data['Defense'].idxmax()]
    print(f"Visaugstākais aizsardzības rādītājs ir Pokémonam {defense['Name']} ar aizsardzības rādītāju {defense['Defense']}.")
if 'Type 2' in data.columns:
    vairaktipi = data[data['Type 2'].notna()].shape[0]
    print(f"Pokemoni, kuriem ir vairāk nekā viens tips: {vairaktipi}.")
