# GeoCoords
GeoCoords é um aplicativo desenvolvido em Python para a visualização e análise de coordenadas geográficas a partir de arquivos CSV ou Excel. O aplicativo permite a leitura de dados, exibição em tabela e geração de mapas interativos com base nas coordenadas fornecidas.

## Funcionalidades
- Importa arquivos CSV ou Excel contendo dados de localização.
- Exibe os dados em uma tabela interativa.
- Gera mapas interativos utilizando a biblioteca Folium.
- Salva os mapas gerados na pasta "mapas" dentro do diretório do projeto.

## O GeoCoords utiliza as seguintes bibliotecas para seu funcionamento:
- openpyxl - Para manipulação de arquivos Excel.
- PySide6 - Interface gráfica.
- PySimpleGUIQt - Construção da interface.
- pandas - Manipulação e análise de dados.
- folium - Geração de mapas interativos.

## Instalação de dependências
- ``pip install -r requerimentos.txt``

## Como Usar
- Execute o arquivo ``app.py``
- Clique em ``Importar`` para selecionar um arquivo CSV ou Excel.
- Clique em ``Vizualizar`` para exibir os dados na tabela.
- Clique em ``Gerar Mapa`` para criar um mapa com as coordenadas presentes no arquivo.
- Os mapas serão gerados na pasta ``mapas`` e poderão serem abertos no navegador.
- ``Importante: No arquivo Excel, as coordenadas de latitude e longitude devem estar formatadas com vírgula (,) em vez de ponto (.), para garantir a correta leitura dos dados pelo aplicativo.``

