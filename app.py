import os
import PySimpleGUIQt as sg
import pandas as pd
from componentes.layout import layout
from componentes.vizualizar_dados import vizualizar_dados
from componentes.gerar_mapa import gerar_mapa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "..", "dados", "dados.xlsx")

def run_app():
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
