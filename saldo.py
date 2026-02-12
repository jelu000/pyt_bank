#Här börjar min kod, en läsare av
import pandas as pd


def main():

# gemini : Istället för att bara titta på texten "Swish", kan du använda df['Belopp'] < 0

    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    
    #läser in inkomster och listar dem
    df = pd.read_csv("../Transaktioner_2026-02-09_16-25-43.csv", encoding="latin-1", skiprows=1, sep=",")
    df = df[['Text', 'Produkt', 'Bokfdag', 'Referens', 'Belopp']]
    swis_inb = df[df["Text"].str.startswith("Swish", na=False)]
    
    print(f'Inkomster:')
    
    df_string = swis_inb.to_string(justify='left', index=False) 
    print(df_string)
    print(f'Total Swish Inkomster: {swis_inb["Belopp"].sum():.2f} kr')

    
    #gemeny- print(swish_in['Belopp'].sum())
    #print(swis_inb)
    
    #Här listar jag de som inte är Swish
    print("\n Här kommer utgifter: \n")
    # HÄMTAR ALLT UTOM SWISH:
    icke_swish = df[~df["Text"].str.startswith("Swish", na=False)]

    print(icke_swish)

main()