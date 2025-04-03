import os
import PySimpleGUIQt as sg
import pandas as pd
import folium
import re
import unicodedata


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "..", "dados", "dados.xlsx")

def vizualizar_dados(caminho):
    try:
        if caminho.endswith('.csv'):
            leitura = pd.read_csv(caminho, encoding='ISO-8859-1')  # Para CSV
        elif caminho.endswith('.xlsx'):
            leitura = pd.read_excel(caminho)  # Para Excel
        else:
            sg.popup_error("Formato de arquivo não suportado. Por favor, selecione um arquivo CSV ou Excel.")
            return pd.DataFrame()
        return leitura
    except Exception as e:
        sg.popup_error(f"Erro ao vizualizar dados: {e}")
        return pd.DataFrame()

def remover_acentos_e_especiais(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r"[!@#$%¨&*()~^´`]", "", texto)
    return texto

def gerar_mapa(nome, latitude, longitude):
    lat_str = str(latitude[0]).replace(",", ".").strip()
    lon_str = str(longitude[0]).replace(",", ".").strip()

    lat = float(lat_str)
    lon = float(lon_str)
    nome = str(nome[0])
    nome = nome.lower()
    nome = remover_acentos_e_especiais(nome)

    print(nome, lat, lon)

    mapa = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup="Belém, Pará").add_to(mapa)
    
    pasta_mapas = os.path.join(os.getcwd(), "mapas")

    if not os.path.exists(pasta_mapas):
        print(f"Erro: A pasta '{pasta_mapas}' não existe.")
        return

    os.chdir(pasta_mapas)

    mapa.save(f"{nome}.html")
    sg.popup("Mapa(s) gerado(s) na pasta MAPAS")

def run_app():
    # configuração do layout
    sg.set_options(background_color="#4CAF50")
    estilo_botao = {"size": (12, 1), "border_width": 2}
    bg_color = sg.theme_background_color()
    estilo_texto = {"font": ("Arial", 10, "bold"), "background_color": bg_color, "text_color": "black"}
    headings = ["ID", "Nome", "Latitude", "Longitude", "Descrição"]
    
    layout = [
        [
            sg.Text("Selecione um Arquivo CSV ou Excel:", **estilo_texto)
        ],
        [
            sg.Input(size=(65, 1), key="-FILE-"), 
            sg.FileBrowse("Importar", size=(12, 1)), 
            sg.Button("Vizualizar", **estilo_botao),
            sg.Button("Gerar Mapa", **estilo_botao)
        ],
        [
            sg.Table(
                values=[[]], 
                headings=headings,
                auto_size_columns=False, 
                justification="center", 
                key="-TABLE-",
                enable_events=True, col_widths=[10, 20, 15, 15, 30], num_rows=10,
                alternating_row_color="lightblue"
            )
        ]     
    ]

    janela = sg.Window("GeoCoords", layout=layout)
  
    while True:
        event, values = janela.read()
        print(event, values)
        
        if event == sg.WIN_CLOSED:
            break
        if event == "Vizualizar":
            caminho =  values["-FILE-"]
            if caminho:
                leitura = vizualizar_dados(caminho)
                if not leitura.empty:
                    valores_tabela = [["id", "nome", "latitude", "longitude", "descricao"]] + leitura.astype(str).values.tolist()
                    janela["-TABLE-"].update(values=valores_tabela)
                else:
                    sg.popup_error("O arquivo está vazio ou não contém dados válidos.")
        
        if event == "Gerar Mapa":
            caminho = values["-FILE-"]
            if caminho:
                dados = pd.read_excel(caminho, usecols=["nome", "latitude", "longitude"])

                nomes = dados["nome"].tolist()
                latitudes = dados["latitude"].astype(float).tolist()
                longitudes = dados["longitude"].astype(float).tolist()

                gerar_mapa(nomes, latitudes, longitudes)

    janela.close()

if __name__ == "__main__":
    run_app()
