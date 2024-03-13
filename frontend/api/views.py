import flet as ft
from .routes import get_notes_api, add_note_api

# def get_notes(page: ft.Page, list_view: ft.ListView):
#     notes = get_notes_api()
#     list_view.items = []  # Reset the list
#     for note in notes:
#         list_view.items.append(ft.ListTile(title=ft.Text(note["content"])))
#     list_view.update()  # Call update without arguments
#     page.update()


def get_notes(page: ft.Page, list_view: ft.ListView):
    notes = get_notes_api()
    print(notes)
    list_view.items = [ft.ListTile(
        title=ft.Text(note["content"])) for note in notes]
    page.update()


def add_note(page: ft.Page, txt_input: ft.TextField, list_view: ft.ListView):
    note_content = txt_input.value
    if note_content:
        note = add_note_api(note_content)
        list_view.items.append(ft.ListTile(title=ft.Text(note["content"])))
        list_view.update()  # Call update without arguments
        page.update()
        txt_input.value = ""  # Clear input after adding
        page.update()
