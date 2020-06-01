#Instalação das bibliotecas
import requests
from bs4 import BeautifulSoup

wiki   = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"

page = requests.get(wiki).text

#print(page)

soup = BeautifulSoup(page,'html5lib')

#print("titulo: ",soup.title)
dataset = []
for tr in soup.select('#mw-content-text .wikitable tbody tr'):
  tds = tr.select('td')
  if len(tds) >= 3 :
    estado = tds[1].get.text().replace('\n','')
    populacao = tds[2].get.text().replace('\n','')
    #print(estado, populacao)
    dataset.append((estado,populacao))

print(dataset)

#salvando como arq csv

with open('Populacao_por_estado.csv','w') as f:
  f.write('"Estado","População"\n')
  for linha in dataset:
    #f.write('"&s","&s"\n' & linha[0],linha[1])
    f.write('"{}","{}"\n' .format(linha[0],linha[1]))
