import os
import PySimpleGUIQt as sg
import folium
import shutil
import re
import unicodedata
from datetime import datetime

data_hora_hoje = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")

def remover_acentos_e_especiais(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r"[!@#$%¨&*()~^´`]", "", texto)
    return texto

def gerar_mapa(nome, latitude, longitude):

    pasta_mapas = os.path.join(os.getcwd(), "mapas")
    if os.path.exists(pasta_mapas):
        shutil.rmtree(pasta_mapas)
    os.makedirs(pasta_mapas)  

    quantidade = len(nome)

    for i in range(quantidade):

        lat_str = str(latitude[i]).replace(",", ".").strip()
        lon_str = str(longitude[i]).replace(",", ".").strip()
        nome_original = str(nome[i])

        lat = float(lat_str)
        lon = float(lon_str)
        nome_cidade = nome_original.lower()
        nome_cidade = remover_acentos_e_especiais(nome_cidade)

        mapa = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup=f"{nome_original}").add_to(mapa)

        pasta_mapas = os.path.join(os.getcwd(), "mapas")
        if not os.path.exists(pasta_mapas):
            os.makedirs(pasta_mapas)
        else:
            caminho_mapa = os.path.join(pasta_mapas, f"{nome_cidade} {data_hora_hoje}.html")
            mapa.save(caminho_mapa)

    sg.popup("Mapa(s) gerado(s) na pasta MAPAS")