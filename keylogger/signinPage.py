import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_username: TextField = TextField(label = 'Username', text_align = ft.TextAlign.LEFT, width = 200)
    text_password: TextField = TextField(label = 'Password', text_align = ft.TextAlign.LEFT, width = 200, password = True)
    checkbox_seePassword: Checkbox = Checkbox(label = 'Show Password', value = False)
    button_login: ElevatedButton = ElevatedButton(text = 'Log In', width = 200, disabled = True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value]):
            button_login.disabled = False
        else:
            button_login.disabled = True
        page.update()
    def showPassword(e: ControlEvent) -> None:
        if (checkbox_seePassword.value):
            text_password.password = False
        else:
            text_password.password = True
        page.update()
    def login(e: ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)

        page.clean()
        page.add(
            Row(
                controls = [Text(value = f'Welcome: {text_username.value}', size = 20)],
                alignment = ft.MainAxisAlignment.CENTER
            )
        )
    
    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_seePassword.on_change = showPassword
    button_login.on_click = login

    page.add(
        Row(
            controls = [
                Column(
                    [text_username,
                     text_password,
                     checkbox_seePassword,
                     button_login]
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )    

if __name__ == '__main__':
    ft.app(main)



        

