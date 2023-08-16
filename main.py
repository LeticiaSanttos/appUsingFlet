import flet as ft
import page_options1
import page_tradutor

def main(page: ft.Page):
    page.title = "Home"

    page.window_center()
    page.window_width = 400

    def go_to_options(e):
        page.route = "/page_options"
        page.update()
    
    
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Login", color=ft.colors.WHITE70),
                              bgcolor=ft.colors.PURPLE_900),
                    ft.TextField(label="Usuário",
                                 border_radius=ft.border_radius.all(20)),
                    ft.TextField(label="Senha", border_radius=ft.border_radius.all(
                        20), password=True, can_reveal_password=True),
                    ft.ElevatedButton("Entrar", width=400, on_click=go_to_options)
                ],
            )
        )
        if page.route == "/page_options":
            page.views.append(
                page_options1.main(page)
            )
        if page.route == "/page_tradutor":
            page.views.append(
                page_tradutor.main(page)
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)