import flet as ft
import page_cadastrar
import page_options1
import page_tradutor
import page_audiodescricao
#import pyrebase

# firebaseConfig = {
#     "apiKey": "AIzaSyAwr-7rc_2PXyk4ztfdE4k1IipmFMOH2ao",
#     "authDomain": "authenticatepy-79282.firebaseapp.com",
#     "projectId": "authenticatepy-79282",
#     "storageBucket": "authenticatepy-79282.appspot.com",
#     "messagingSenderId": "53401536333",
#     "appId": "1:53401536333:web:db5e1ae5ba73ba49459904",
#     "measurementId": "G-F0NDZNRXTH",
#     "databaseURL": ""
#   }

# firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()



def main(page: ft.Page):
    page.title = "Login Page"

    page.window_center()
    page.window_width = 400

    def go_to_cadastrar(e):
        page.route = "/page_cadastrar"
        page.update()

    def go_to_options(e):
        page.route = "/page_options"
        page.update()
    
    def close_banner(e):
        my_baner.open = False
        page.update()

    txt_title = ft.Text("Login", 
                        color= ft.colors.WHITE70,
                        weight=ft.FontWeight.BOLD,
                        size=46)
    
    txt_email = ft.TextField(
        label="Email",
        color=ft.colors.WHITE70,
        border_color=ft.colors.WHITE,
        multiline=True,
        height=80,
        width=350
    )

    txt_senha = ft.TextField(
        label="Senha",
        password=True, 
        can_reveal_password=True,
        color=ft.colors.WHITE70,
        border_color=ft.colors.WHITE,
        multiline=True,
        height=80,
        width=350
    )
    
    page.banner = ft.Banner(
        bgcolor=ft.colors.RED_200,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_300, size=40),
        content=ft.Text(
            "Email ou senha incorretos!"
        ),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )
    my_baner = page.banner;

    def login(e):
        email = txt_email.value
        senha = txt_senha.value
   
        # try: 
        #     user = auth.sign_in_with_email_and_password(email, senha)
        go_to_options(e)
        print("Logado com sucesso!")
        # except:
        #     my_baner.open = True
        #     page.update()
        #     print("Email ou senha incorretos!")


    btn_login = ft.ElevatedButton(
        text="Entrar",
        width=350,
        #bgcolor="#6800E3",
        bgcolor={ft.MaterialState.HOVERED: "#A11D8A", "": "#6800E3"},
        color=ft.colors.WHITE,
        on_click=login,
    )

    

    btn_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        width=350,
        bgcolor="#6800E3",
        color=ft.colors.WHITE,
        on_click=go_to_cadastrar,
    )

    ct_baner = ft.Container(
        content=my_baner
    )
    
    ct_title = ft.Container(
        content=txt_title,
        alignment=ft.alignment.center
    )

    ct_email = ft.Container(
        content=txt_email,
        alignment=ft.alignment.center
    )

    ct_senha = ft.Container(
        content=txt_senha,
        alignment=ft.alignment.center
    )

    ct_login = ft.Container(
        content=btn_login,
        alignment=ft.alignment.center
    )

    ct_cadastrar = ft.Container(
        content=btn_cadastrar,
        alignment=ft.alignment.center
    )


    coluna = ft.Column(
        controls=[
            ct_baner,
            ct_title,
            ct_email,
            ct_senha,
            ct_login,
            ct_cadastrar,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    main_container = ft.Container(
        content=coluna,
        width=400,
        height=660,
        border_radius=25,
        bgcolor= "#260053",
        padding=12
    )
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    main_container
                ],
            )
        )
        if page.route == "/page_cadastrar":
            page.views.append(
                page_cadastrar.main(page)
            )
        if page.route == "/page_options":
            page.views.append(
                page_options1.main(page)
            )
        if page.route == "/page_tradutor":
            page.views.append(
                page_tradutor.main(page)
            )
        if page.route == "/page_audio":
            page.views.append(
                page_audiodescricao.main(page)
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.update()
ft.app(target=main)
#ft.app(target=main, view=ft.WEB_BROWSER)
