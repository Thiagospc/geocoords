import os
import PySimpleGUIQt as sg
import pandas as pd
import openpyxl
import folium


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "..", "arquivos", "dados.xlsx")

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

def criar_arquivo_se_necessario():
    if not os.path.exists(CAMINHO_ARQUIVO):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["ID", "Nome", "Latitude", "Longitude", "Descrição"])
        wb.save(CAMINHO_ARQUIVO)
    
def adicionar_no_excel(id, nome, latitude, longitude, descricao):
    try:
        criar_arquivo_se_necessario()
        
        df = pd.read_excel(CAMINHO_ARQUIVO, dtype={"ID": int, "Latitude": float, "Longitude": float, "Descrição": str})
        id = str(id).strip()
        latitude = float(latitude)
        longitude = float(longitude)
        descricao = str(descricao).strip()
        
        if id in df["ID"].astype(str).values:
            sg.popup_error(f"Erro: O ID {id} já existe no arquivo.")
            return
        
        nova_linha = pd.DataFrame([[id, nome, latitude, longitude, descricao]], columns=df.columns)
        
        df = pd.concat([df, nova_linha], ignore_index=True)
        df.to_excel(CAMINHO_ARQUIVO, index=False)
        sg.popup("Dados adicionados com sucesso!")    
        
    except ValueError:
        sg.popup_error("Erro: Certifique-se de que latitude e longitude são números válidos.")
    except Exception as e:
        sg.popup_error(f"Erro ao adicionar dados: {e}")

def exibe_mapa(df):
    pass

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
            sg.Text("Editar Linha (id, nome, latitude, longitude, descricao):", **estilo_texto)
        ],
        [
            sg.Input(size=(5, 1), key="-ID-"), 
            sg.Input(size=(15, 1), key="-NOME-"),
            sg.Input(size=(10, 1), key="-LATITUDE-"), 
            sg.Input(size=(10, 1), key="-LONGITUDE-"),
            sg.Input(size=(25, 1), key="-DESCRICAO-"),
            sg.Button("Adicionar", **estilo_botao),
            sg.Button("Editar", **estilo_botao),   
            sg.Button("Salvar Edição", **estilo_botao)
            
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

        if event == "Adicionar":
            id_ = values["-ID-"]
            nome = values["-NOME-"]
            latitude = values["-LATITUDE-"]
            longitude = values["-LONGITUDE-"]
            descricao = values["-DESCRICAO-"]

            if id_ and nome and latitude and longitude and descricao:
                adicionar_no_excel(id_, nome, latitude, longitude, descricao)
                
            leitura = vizualizar_dados(CAMINHO_ARQUIVO)
            if not leitura.empty:
                valores_tabela = leitura.astype(str).values.tolist()
                janela["-TABLE-"].update(values=valores_tabela)

            else:
                sg.popup_error("Preencha todos os campos antes de adicionar.")
        
        if event == "Editar":
            print("Editar")
            
        if event == "Salvar Edição":
            print("Salvar Edição")
            
        if event == "Gerar Mapa":
            print("Gerar Mapa")

    janela.close()

if __name__ == "__main__":
    run_app()
