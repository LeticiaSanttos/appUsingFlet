import flet as ft
import time
import sys
#import keyboard as kb
#sys.path.insert(1, "./functions")
import functions.transcricao as tr
import functions.audio as ad

def main(page: ft.Page):
    
    caminho = ""

    def go_to_options(e):
        page.route = "/page_options"
        page.update()

    img_audiod = ft.Image(
        src=f"images/writting.png",
        width=40,
        height=40,
        color= ft.colors.PURPLE_400,
    )

    txt_title = ft.Text("Transcrição de Áudio", 
                        color= ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        size=18)
    
    txt_texto = ft.Text("",
                            weight=ft.FontWeight.BOLD,
                            expand=True,
                            color=ft.colors.WHITE70,
                            size=20)
    def transcricao(e):
        txt_texto.value = tr.transcrever()
        print(txt_texto.value)
        page.update()


    def exibeAudio(e):
        tr.ouvir()
  
    btn_gravar = ft.ElevatedButton(
        text="Gravar Áudio", 
        icon=ft.icons.MIC, 
        on_click= transcricao
        )

    btn_audio = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.MIC,
        tooltip="Ouvir texto",
        bgcolor=ft.colors.WHITE10,
        on_click=exibeAudio
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
    
    container_txt_texto = ft.Container(
        content=ft.Row([
            txt_texto,
            btn_audio
        ]),
        height=320,
        bgcolor="#490596",
        alignment=ft.alignment.top_left,
        border_radius=20,
        padding= 10,
        margin=7
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
        spacing=30
        ), 
        alignment=ft.alignment.top_left
    )
    
    ct_gravar = ft.Container(
        content=ft.Row(
        [btn_gravar],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

    clm_header = ft.Column(
        controls= [
            ct_title,
            ct_gravar,
            container_txt_texto
            
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
        "/page_transcricao",
        [
            main_container
        ]
    )

    return view