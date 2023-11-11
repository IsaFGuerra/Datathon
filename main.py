import pandas as pd
import matplotlib.pyplot as plt

def main():
    #Opening data files 
    file_path_temperatures = "dados/Annual_Surface_Temperature_Change.csv"
    file_path_pesticides = "dados/pesticide-use-tonnes.csv"

    temperatures = pd.read_csv(file_path_temperatures)
    pesticides = pd.read_csv(file_path_pesticides)
    
    print(pesticides)
    print(temperatures)

    temperatures.to_excel("temperatures.xlsx", index=True)

    pesticides = clean_columns_pesticides(pesticides)
    #limpa_temperatura(temperatura)

    merged_df = pd.merge(temperatures, pesticides, left_on='ISO3', right_on='Code', how='inner')

    merged_df.to_excel("arquivo_merge.xlsx", index=True)

    # We normalized and treated the data in Excel, at the most part
    merged_treated = pd.read_excel("dados_tratados\Dados_tratados_normalizados.xlsx")

    print(merged_treated)

    # graph
    create_graphs(merged_treated)

def create_graphs(df:pd.DataFrame):
    # Create list of countrys
    countrys = df["País"].tolist()

    # Create list of years
    years = []
    for year in range(1990,2021):
        years.append(year)
        
    # Create dictionary
    # Key = country
    # dict[0] = [list_of_pesticides]
    # dict[]
    print(countrys)
    print(years)

    # AT THE END WE DECIDED TO MAKE THE GRAPHS INSIDE THE EXCEL

# Países - Consumos agro - anos - temperatura




def clean_columns_pesticides(df: pd.DataFrame):

    #Removes the lines where the "Code" column is "Nan" as they are not countries
    df = df[df["Code"].notna()]

    # Filters useful    df = df[['Entity', 'Code' , 'Year', 'Pesticides (total)']]

    #Removes the semicolons and cleans the data in the pesticides table 
    remover_ponto_virgula = lambda x: x.replace(";", "") if isinstance(x, str) else x

    df['Pesticides (total)'] = df['Pesticides (total)'].apply(remover_ponto_virgula)

    df['Pesticides (total)'] = df['Pesticides (total)'].astype(float)

    print(df)

    # Pivots table
    tabela_pivotada = df.pivot(index='Code', columns='Year', values='Pesticides (total)')

    # Renomeia as 
    tabela_pivotada.columns.name = None

    print(tabela_pivotada)
    tabela_pivotada.to_excel("tabela_pivotada.xlsx", index=True)

    return tabela_pivotada

# Used to verify open database data
def clean_columns_temperature(df: pd.DataFrame):
    print("Nome das colunas: ")

    colunas = df.columns.tolist()

    colunas_anos = []
    for coluna in colunas:
        if coluna.startswith("F"):
            colunas_anos.append(coluna)

    media = df[colunas_anos].mean()

    media.to_excel("media.xlsx")
if _name_ == "_main_":
    main()