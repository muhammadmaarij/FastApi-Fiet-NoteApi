# import flet
# from flet import TextField, ElevatedButton, Page


# def main(page: Page):
#     def login_click(e):
#         # Logic to handle login
#         pass

#     page.add(
#         TextField(label="Username"),
#         TextField(label="Password", password=True),
#         ElevatedButton("Login", on_click=login_click)
#     )


# flet.app(target=main)
import flet as ft
from api.routes import setup_routes

def main(page: ft.Page):
    setup_routes(page)

if __name__ == "__main__":
    ft.app(target=main)
