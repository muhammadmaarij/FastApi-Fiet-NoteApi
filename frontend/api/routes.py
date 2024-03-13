# from views import note_view, login_view

# def setup_routes(page):
#     # Example route setup - you can expand this with actual routing logic
#     page.add(note_view())
#     # To add more routes, you'd call the corresponding view functions here

import requests


def get_notes_api():
    response = requests.get("http://127.0.0.1:8000/notes/")
    notes = response.json()
    return notes


def add_note_api(content):
    response = requests.post(
        "http://127.0.0.1:8000/notes/", json={"content": content})
    note = response.json()
    return note
