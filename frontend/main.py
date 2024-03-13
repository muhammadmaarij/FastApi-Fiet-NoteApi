# # import flet
# # from flet import TextField, ElevatedButton, Page


# # def main(page: Page):
# #     def login_click(e):
# #         # Logic to handle login
# #         pass

# #     page.add(
# #         TextField(label="Username"),
# #         TextField(label="Password", password=True),
# #         ElevatedButton("Login", on_click=login_click)
# #     )


# # flet.app(target=main)
# import flet as ft
# from api.routes import setup_routes

# def main(page: ft.Page):
#     setup_routes(page)

# if __name__ == "__main__":
#     ft.app(target=main)
import flet as ft
from .api.views import get_notes, add_note


def main(page: ft.Page):
    txt_input = ft.TextField(hint_text="Enter your note", autofocus=True)
    btn_add = ft.ElevatedButton(
        text="Add Note", on_click=lambda e: add_note(page, txt_input, list_view))
    list_view = ft.ListView()

    # Initial load of notes
    get_notes(page, list_view)

    page.add(txt_input, btn_add, list_view)


if __name__ == "__main__":
    ft.app(target=main)
