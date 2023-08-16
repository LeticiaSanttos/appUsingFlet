import flet as ft 

def main(page):
     
    def go_to_tradutor(e):
        page.route = "/page_tradutor"
        page.update()

    def go_to_audiodescricao(e):
        page.route = "/page_audio"
        page.update()
        

    img_audio_to_txt = ft.Image(
        src="images/writting.png",
        width=80,
        height=80,
        color= "#A11D8A",
        
    )

    btn_audio_to_txt = ft.ElevatedButton(
        text="Converter Áudio em Texto", 
        width=250,
        bgcolor="#6800E3",
        color=ft.colors.WHITE
        
        )

    img_txt_to_audio = ft.Image(
        src="images/speaking.png",
        width=80,
        height=80,
        color= "#A11D8A",    
    )

    btn_txt_to_audio = ft.ElevatedButton(
        "Converter Texto em Áudio", 
        on_click=go_to_audiodescricao,
        width=250,
        bgcolor="#6800E3",
        color=ft.colors.WHITE
        
        )

    img_translate = ft.Image(
        src="images/translation.png",
        width=100,
        height=100,
        color= "#A11D8A",
        
    )

    btn_translate = ft.ElevatedButton(
        text="Tradutor de Mensagens", 
        on_click=go_to_tradutor,
        width=250,
        bgcolor="#6800E3",
        color=ft.colors.WHITE
        
        )


    container_audio_to_txt = ft.Container(
        content=img_audio_to_txt,
        alignment=ft.alignment.center,
    )

    container_btn_audio_to_txt = ft.Container(
        content=btn_audio_to_txt,
        alignment=ft.alignment.center
    )

    container_txt_to_audio = ft.Container(
        content=img_txt_to_audio,
        alignment=ft.alignment.center,
    )

    container_btn_txt_to_audio = ft.Container(
        content=btn_txt_to_audio,
        alignment=ft.alignment.center,
    )

    container_translate= ft.Container(
        content=img_translate,
        alignment=ft.alignment.center,
    )

    container_btn_translate = ft.Container(
        content=btn_translate,
        alignment=ft.alignment.center,
    )

    

    coluna = ft.Column(
        controls=[container_audio_to_txt, 
                  container_btn_audio_to_txt,
                  container_txt_to_audio,
                  container_btn_txt_to_audio,
                  container_translate,
                  container_btn_translate],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing=30
        
    )

    main_container = ft.Container(
        content=coluna,
        width=400,
        height=660,
        border_radius=25,
        bgcolor= "#260053"
    )

    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(
    #         ft.View(
    #             "/",
    #             [
    #                 main_container
    #             ],
    #         )
    #     )
    #     if page.route == "/page_tradutor":
    #         page.views.append(
    #             page_tradutor.main(page)
    #         )
    #     page.update()

    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    # page.on_route_change = route_change
    # page.on_view_pop = view_pop
    # page.go(page.route)

    view = ft.View(
        "/page_options",
        [
            main_container
        ]
    )

    return view