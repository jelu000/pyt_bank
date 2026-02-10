#Här börjar min kod, en läsare av
import pandas as pd


def main():

    df = pd.read_csv("../Transaktioner_2026-02-09_16-25-43.csv", encoding="latin-1", skiprows=1, sep=",")
    swis_inb = df[df["Text"].str.startswith("Swish", na=False)]
    
    print(f'Inkomster:')
    print(swis_inb)
    print("\n Här kommer utgifter: \n")
    # HÄMTAR ALLT UTOM SWISH:
    icke_swish = df[~df["Text"].str.startswith("Swish", na=False)]

    print(icke_swish)



main()