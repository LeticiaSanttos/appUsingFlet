import flet as ft
import time
import sys
#import keyboard as kb
#sys.path.insert(1, "./functions")
import functions.audio as ad
import functions.image as img

def main(page: ft.Page):
    
    caminho = ""

    def go_to_options(e):
        page.route = "/page_options"
        page.update()

    img_audiod = ft.Image(
        src=f"images/speaking.png",
        width=40,
        height=40,
        color= ft.colors.PURPLE_400,
    )

    txt_title = ft.Text("Audiodescrição", 
                        color= ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        size=18)

    #uso dos dados do arquivo
    def pick_files_result(e: ft.FilePickerResultEvent):
        
          caminho =  (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
          );
    
          selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
          )
          #caminho.update()
          resp.value = img.camImagem(caminho)
          resp.update()
          selected_files.update()
        
    #botao para abrir o arquivo
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text(
        color=ft.colors.WHITE,
        size= 12,
        text_align= ft.alignment.center
    )
    
    # #caminho do arquivo
    # caminho = ft.Text(
    #     color=ft.colors.WHITE,
    #     size= 15,
    #     text_align= ft.alignment.center
    # )
    def audio(e):
         ad.audiodescricao(resp.value)
    
    def audio2(e):
         ad.audiodescricao(txt_digita.value)
    #texto extraído da imagem
    resp = ft.Text(
        color=ft.colors.WHITE,
        size= 12,
        text_align= ft.alignment.center
    )
    textoImg = resp.value

    btn_abrirImg = ft.ElevatedButton(
        text="Escolher Imagem", 
        icon=ft.icons.UPLOAD, 
        on_click=lambda _: pick_files_dialog.pick_files(
        allow_multiple=True,
        file_type= ft.FilePickerFileType.IMAGE
    ))

    page.overlay.append(pick_files_dialog)

    btn_audio = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.MIC,
        tooltip="Ouvir texto",
        bgcolor=ft.colors.WHITE10,
        on_click=audio
    )

    title = ft.Container(
        content=ft.Row(
        [img_audiod, txt_title],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
        ),
        alignment=ft.alignment.center,
        padding=10
    )

    btn_voltar = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.NAVIGATE_BEFORE,
        tooltip="Voltar para a tela Opções",
        bgcolor=ft.colors.WHITE10,
        on_click=go_to_options,
    )
  
    ct_title = ft.Container(
        content= ft.Row(
        [btn_voltar,title],
        spacing=45
        ), 
        alignment=ft.alignment.top_left
    )
    
    txt_digita = ft.TextField(
        label="Digite o Texto",
        border_color=ft.colors.WHITE,
        color= ft.colors.WHITE,
        multiline=True,
        height=60,
        width=200,
        text_size=12
        )
    
    btn_audio2 = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.MIC,
        tooltip="Ouvir texto",
        bgcolor=ft.colors.WHITE10,
        on_click=audio2
    )
    
    ct_opcoes = ft.Container(
        content=ft.Row(
        [btn_abrirImg, btn_audio],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

    legenda1 = ft.Text("Escolha a imagem que deseja extrair o texto:", color=ft.colors.WHITE)
    legenda2 = ft.Text("Digite o texto que deseja converter em audio:", color=ft.colors.WHITE)

    clm_texto = ft.Column(
        controls= [
            selected_files,
            resp
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=True
    )
    
    ct_digita = ft.Container(
        content=ft.Row(
        [txt_digita, btn_audio2],
        alignment=ft.MainAxisAlignment.START
        )
    )
    
    ct_texto = ft.Container(
        content=clm_texto,
        height=350,
        bgcolor="#490596",
        alignment=ft.alignment.top_left,
        border_radius=20,
        padding= 10,
        margin=7
    )
    clm_header = ft.Column(
        controls= [
            ct_title,
            legenda1,
            ct_opcoes,
            ct_texto,
            legenda2,
            ct_digita
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=True
    )

    main_container = ft.Container(
        content=clm_header,
        width=400,
        height=660,
        border_radius=25,
        bgcolor= "#260053",
        padding=12
    )
     
    view = ft.View(
        "/page_audio",
        [
            main_container
        ]
    )

    return view