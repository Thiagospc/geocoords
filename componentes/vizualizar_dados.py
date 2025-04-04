import PySimpleGUIQt as sg
import pandas as pd

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