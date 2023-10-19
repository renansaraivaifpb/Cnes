url_state_mapping = {
    12: 'ACRE',
    27: 'ALAGOAS',
    13: 'AMAZONAS',
    16: 'AMAPA',
    29: 'BAHIA',
    23: 'CEARA',
    53: 'DISTRITO FEDERAL',
    32: 'ESPIRITO SANTO',
    52: 'GOIAS',
    21: 'MARANHAO',
    31: 'MINAS GERAIS',
    50: 'MATO GROSSO DO SUL',
    51: 'MATO GROSSO',
    15: 'PARA',
    25: 'PARAIBA',
    26: 'PERNAMBUCO',
    22: 'PIAUI',
    41: 'PARANA',
    33: 'RIO DE JANEIRO',
    24: 'RIO GRANDE DO NORTE',
    11: 'RONDONIA',
    14: 'RORAIMA',
    43: 'RIO GRANDE DO SUL',
    42: 'SANTA CATARINA',
    28: 'SERGIPE',
    35: 'SAO PAULO',
    17: 'TOCANTINS'
}
url = ['https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=12&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=27&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=13&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=78&VTipo_Leito=3&VListar=1&VEstado=16&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=29&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=23&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=53&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=32&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=52&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=21&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=31&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=50&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=51&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=15&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=25&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=26&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=22&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=41&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=33&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=24&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=11&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=14&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=43&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=42&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=28&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=35&VMun=&VComp=',
'https://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=77&VTipo_Leito=3&VListar=1&VEstado=17&VMun=&VComp=']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
# Create an empty list to store dataframes
all_dataframes = []

for i in range(len(url)):
    page = requests.get(url[i], headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the rows <tr> with bgcolor='#cccccc'
    linhas_com_bgcolor = soup.find_all('tr', {'bgcolor': '#cccccc'})

    # Initialize lists to store values
    cnes = []
    estabelecimento = []
    municipios = []
    existentes = []
    sus = []

    # Get the state code from the URL
    estado_code = int(url[i].split('VEstado=')[1].split('&')[0])
    
    # Get the state name based on the state code
    estado_name = url_state_mapping.get(estado_code, 'Unknown')

    # Iterate through the found rows
    for linha in linhas_com_bgcolor:
        # Find all <td> cells within the row
        celulas = linha.find_all('td')

        # Get values from cells and remove leading and trailing whitespace
        valor_cnes = celulas[0].find('font').text.strip()
        valor_estabelecimento = celulas[1].find('font').text.strip()
        valor_municipio = celulas[2].find('font').text.strip()
        valor_existentes = celulas[3].find('font').text.strip()
        valor_sus = celulas[4].find('font').text.strip()

        # Add values to the respective lists
        cnes.append(valor_cnes)
        estabelecimento.append(valor_estabelecimento)
        municipios.append(valor_municipio)
        existentes.append(valor_existentes)
        sus.append(valor_sus)

    # Create a DataFrame with the lists of values and add 'Estado' column
    data = {'CNES': cnes, 'Estabelecimento': estabelecimento, 'Municipios': municipios, 'Existentes': existentes, 'SUS': sus, 'Estado': estado_name}
    df = pd.DataFrame(data)

    # Append the dataframe to the list of dataframes
    all_dataframes.append(df)

# Concatenate all dataframes into one
final_dataframe = pd.concat(all_dataframes, ignore_index=True)

# Save the final dataframe to a CSV file
final_dataframe.to_csv('UTI PEDIATRICA - TIPO I.csv', index=False)
