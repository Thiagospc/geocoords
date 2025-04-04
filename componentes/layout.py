import PySimpleGUIQt as sg

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