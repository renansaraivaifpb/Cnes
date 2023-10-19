# BIBLIOTECAS
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://cnes2.datasus.gov.br/Mod_Ind_Leitos_Listar.asp?VCod_Leito=80&VTipo_Leito=3&VListar=1&VEstado=00&VMun=&VComp='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')


# Encontre todas as linhas <tr> com bgcolor='#cccccc'
linhas_com_bgcolor = soup.find_all('tr', {'bgcolor': '#cccccc'})

# Inicialize listas para armazenar os valores
cnes = []
estabelecimento = []
existentes = []
sus = []

# Itere pelas linhas encontradas
for linha in linhas_com_bgcolor:
    # Encontre todas as células <td> dentro da linha
    celulas = linha.find_all('td')
    
    # Obtenha os valores das células e remova os espaços em branco no início e no final
    valor_cnes = celulas[0].find('font').text.strip()
    valor_estabelecimento = celulas[1].find('a').text.strip()
    valor_existentes = celulas[2].find('font').text.strip()
    valor_sus = celulas[3].find('font').text.strip()
    
    # Adicione os valores às listas correspondentes
    cnes.append(valor_cnes)
    estabelecimento.append(valor_estabelecimento)
    existentes.append(valor_existentes)
    sus.append(valor_sus)

# Crie um DataFrame com as listas de valores
data = {'CNES': cnes, 'Estabelecimento': estabelecimento, 'Existentes': existentes, 'SUS': sus}
df = pd.DataFrame(data)

# Imprima o DataFrame
print(df)

# Salvar df com informações gerais
df.to_csv('df.csv', index=False)
