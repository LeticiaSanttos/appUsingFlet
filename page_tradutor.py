import flet as ft
import time
import sys
#import keyboard as kb
#sys.path.insert(1, "./functions")
import functions.f_tradutor as td
import functions.audio as ad

def main(page: ft.Page):

    def go_to_options(e):
        page.route = "/page_options"
        page.update()
    
    img_translate = ft.Image(
        src=f"images/translation.png",
        width=40,
        height=40,
        color= ft.colors.PURPLE_400,
    )

    txt_title = ft.Text("Tradutor", 
                        color= ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        size=18)
    
    btn_voltar = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.NAVIGATE_BEFORE,
        tooltip="Voltar para a tela Opções",
        bgcolor=ft.colors.WHITE10,
        on_click=go_to_options,
    )
  
    title = ft.Container(
        content= ft.Row(
        [img_translate, txt_title ],
        spacing=5
        ),
        alignment=ft.alignment.center,
        padding=8
    )
    
    ct_title = ft.Container(
        content= ft.Row(
        [btn_voltar,title ],
        spacing=55
        ), 
        alignment=ft.alignment.top_left
    )

    def exibeAudio(e):
        print('audio')
        idioma = td.Tradutor.verifica_idioma(to_lang)
        print(idioma)
        ad.audiodescricao(txt_traduzido.value, idioma)
        

    def terminou_de_digitar(e):
        if frase.value.endswith(" "):
            terminou = False
        else:
            terminou = True

        return terminou

    def traduz(e): 
        if frase.value != "":
            time.sleep(1.5)
            if terminou_de_digitar(e) == True:
                traducao = td.Tradutor(td.Tradutor.verifica_idioma(from_lang),td.Tradutor.verifica_idioma(to_lang), frase.value)
                txt_traduzido.value = traducao.traduzir()
                page.update()
        else:
            txt_traduzido.value = ""
            page.update()

    from_lang=ft.Dropdown(
        label="Traduzir de",
        width=350,
        filled=True,
        border_color=ft.colors.WHITE,
        focused_bgcolor=ft.colors.PURPLE_400,
        focused_color=ft.colors.BLACK,
        options=[
            ft.dropdown.Option("Inglês"),
            ft.dropdown.Option("Português"),
            ft.dropdown.Option("Chinês"),
            ft.dropdown.Option("Espanhol"),
            ft.dropdown.Option("Francês"),
            ft.dropdown.Option("Árabe"),
            ft.dropdown.Option("Russo"),
        ],
        on_change=traduz
        )
    

    to_lang=ft.Dropdown(
        label="Traduzir para",
        width=350,
        filled=True,
        border_color=ft.colors.WHITE,
        focused_bgcolor=ft.colors.PURPLE_400,
        focused_color=ft.colors.BLACK,
        options=[
            ft.dropdown.Option("Inglês"),
            ft.dropdown.Option("Português"),
            ft.dropdown.Option("Chinês"),
            ft.dropdown.Option("Espanhol"),
            ft.dropdown.Option("Francês"),
            ft.dropdown.Option("Árabe"),
            ft.dropdown.Option("Russo"),
        ],
        on_change=traduz
        )
    
    ltb_from_lang = ft.Container(
        content=from_lang,
        alignment=ft.alignment.center,
        #bgcolor="#F0F2F5",
        #border_radius=5,
    )

    ltb_to_lang = ft.Container(
        content=to_lang,
        alignment=ft.alignment.center,
        # bgcolor="#F0F2F5",
        # border_radius=5
    )
   
    frase = ft.TextField(
        label="Digite o Texto",
        border_color=ft.colors.WHITE,
        color= ft.colors.WHITE,
        multiline=True,
        height=80,
        width=350,
        on_change=traduz
        )

    tb_entrada = ft.Container(
        content=frase,
        alignment=ft.alignment.center
    )

    txt_traduzido = ft.Text("",
                            weight=ft.FontWeight.BOLD,
                            expand=True,
                            color=ft.colors.WHITE70,
                            size=20)
    
    btn_audio = ft.IconButton(
        icon_color=ft.colors.PURPLE_400,
        icon=ft.icons.MIC,
        tooltip="Ouvir texto",
        bgcolor=ft.colors.WHITE10,
        on_click=exibeAudio
    )

    container_txt_traduzido = ft.Container(
        content=ft.Row([
            txt_traduzido,
            btn_audio
        ]),
        height=320,
        bgcolor="#490596",
        alignment=ft.alignment.top_left,
        border_radius=20,
        padding= 10,
        margin=7
    )


    coluna = ft.Column(
        controls=[
           # btn_voltar,
            #clm_voltar,
            ct_title,
            ltb_from_lang,
            ltb_to_lang,
            tb_entrada,
            container_txt_traduzido
        ],
        alignment=ft.MainAxisAlignment.START,
        
    )

    main_container = ft.Container(
        content=coluna,
        width=400,
        height=660,
        border_radius=25,
        bgcolor= "#260053",
        padding=12
    )
     
    view = ft.View(
        "/page_tradutor",
        [
            main_container
        ]
    )

    return view