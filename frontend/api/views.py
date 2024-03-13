from flet import TextField, ElevatedButton, ListView, UserControl


def note_view():
    txt_input = TextField()
    btn_add = ElevatedButton(text="Add Note")
    list_notes = ListView()

    # Assemble the note-taking view
    return UserControl(controls=[txt_input, btn_add, list_notes])


def login_view():
    txt_username = TextField(label="Username")
    txt_password = TextField(label="Password", password=True)
    btn_login = ElevatedButton(text="Login")

    # Assemble the login view
    return UserControl(controls=[txt_username, txt_password, btn_login])
