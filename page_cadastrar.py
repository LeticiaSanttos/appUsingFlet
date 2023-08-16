import flet as ft
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAwr-7rc_2PXyk4ztfdE4k1IipmFMOH2ao",
    "authDomain": "authenticatepy-79282.firebaseapp.com",
    "projectId": "authenticatepy-79282",
    "storageBucket": "authenticatepy-79282.appspot.com",
    "messagingSenderId": "53401536333",
    "appId": "1:53401536333:web:db5e1ae5ba73ba49459904",
    "measurementId": "G-F0NDZNRXTH",
    "databaseURL": ""
  }

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def main(page):

    def go_to_login(e):
        page.route = "/"
        page.update()

    def close_banner(e):
        my_baner.open = False
        page.update()

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
        color=ft.colors.WHITE70,
        border_color=ft.colors.WHITE,
        multiline=True,
        height=80,
        width=350
    )

    page.banner = ft.Banner(
        bgcolor=ft.colors.RED_200,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_300, size=40),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )
    my_baner = page.banner;

    def cadastrar(e):
        email = txt_email.value
        senha = txt_senha.value

        

        try:
            # if auth.sign_in_with_email_and_password(email, senha):
            #    my_baner.content = ft.Text("Esse usuário já está cadastrado!")
            #    my_baner.open = True
            #    page.update()
               
            user = auth.create_user_with_email_and_password(email, senha)
            print("Usuário cadastrado com sucesso!")
        except:
               my_baner.content = ft.Text("Preencha os dados de forma correta!")
               my_baner.open = True
               page.update()

        # try:
        #     if auth.sign_in_with_email_and_password(email, senha):
        #        my_baner.content = ft.Text("Esse usuário já está cadastrado!")
        #        my_baner.open = True
        #        page.update()
        #     else:   
        #        user = auth.create_user_with_email_and_password(email, senha)
        #        print("Usuário cadastrado com sucesso!")
        # except Exception.args. as error:
        #         my_baner.content = ft.Text("Preencha os dados de forma correta!")
        #         my_baner.open = True
        #         page.update()

    txt_title = ft.Text("Cadastro", 
                        color= ft.colors.WHITE70,
                        weight=ft.FontWeight.BOLD,
                        size=46)

    btn_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        width=350,
        bgcolor="#6800E3",
        color=ft.colors.WHITE,
        on_click=cadastrar
    )

    btn_possui_conta = ft.ElevatedButton(
        text="Já possui uma conta? Entre Aqui",
        width=350,
        bgcolor="#6800E3",
        color=ft.colors.WHITE,
        on_click=go_to_login,
                            )

    ct_email = ft.Container(
        content=txt_email,
        alignment=ft.alignment.center
    )

    ct_senha = ft.Container(
        content=txt_senha,
        alignment=ft.alignment.center
    )

    ct_title = ft.Container(
        content=txt_title,
        alignment=ft.alignment.center
    )

    ct_cadastrar = ft.Container(
        content=btn_cadastrar,
        alignment=ft.alignment.center
    )

    ct_possui_conta = ft.Container(
        content=btn_possui_conta,
        alignment=ft.alignment.center
    )


    coluna = ft.Column(
        controls=[
            ct_title,
            ct_email,
            ct_senha,
            ct_cadastrar,
            ct_possui_conta,
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

    page.update()
    

    view = ft.View(
        "/page_cadastrar",
        [
            main_container
        ]
    )

    return view