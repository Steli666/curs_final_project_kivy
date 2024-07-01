import re
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import requests
from kivymd.uix.dialog import MDDialog
from All import token_store

class Register(Screen):
    def next(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")
        self.ids.email.text_color = app.theme_cls.primary_color
        self.ids.Email.text_color = app.theme_cls.primary_color
        self.ids.email.icon = "check-decagram"

    def previous(self):
        self.ids.slide.load_previous()
        self.ids.email.text_color = (0, 0, 0, 1)
        self.ids.Email.text_color = (0, 0, 0, 1)
        self.ids.email.icon = "numeric-1-circle"

    def next1(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")
        self.ids.password.text_color = app.theme_cls.primary_color
        self.ids.Password.text_color = app.theme_cls.primary_color
        self.ids.password.icon = "check-decagram"

    def next2(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")
        self.ids.submit.text_color = app.theme_cls.primary_color
        self.ids.Submit.text_color = app.theme_cls.primary_color

    def validate_inputs(self):
        email = self.ids.email1
        username = self.ids.username
        password = self.ids.password1
        password_confirm = self.ids.confirm_password

        valid = True

        if not email.text or not self.check_email(email.text):
            self.show_error(email)
            valid = False
        else:
            self.clear_error(email)

        if not password.text:
            self.show_error(password)
            valid = False
        else:
            self.clear_error(password)

        if not password_confirm.text:
            self.show_error(password_confirm)
            valid = False
        else:
            self.clear_error(password_confirm)

        if password.text != password_confirm.text:
            self.show_error(password)
            self.show_error(password_confirm)
            valid = False
        else:
            self.clear_error(password)
            self.clear_error(password_confirm)

        if not username.text:
            self.show_error(username)
            valid = False
        else:
            self.clear_error(username)

        return valid

    def check_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        return False

    def show_error(self, widget):
        widget.error = True
        widget.text_color = (1, 0, 0, 1)  # Red color for error

    def clear_error(self, widget):
        widget.error = False
        widget.text_color = (0, 0, 0, 1)  # Black color when no error

    def register(self):
        if not self.validate_inputs():
            return

        email = self.ids.email1.text
        username = self.ids.username.text
        password = self.ids.password1.text
        data = {
            "email": email,
            "username": username,
            "password": password
        }

        url = "http://127.0.0.1:8000/api/register"
        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                self.switch_screen("home")
                token_response = response.json()
                print(token_response)
                token_store.put("vars", token="Token " + token_response.get("token"))
            else:
                dialog = MDDialog(
                    title="Username or email already used",
                    text="Please try another.",
                    size_hint=(0.8, 0.4),
                )
                dialog.elevation = 0
                dialog.open()
                print("Failed to fetch sessions. Status code:", response.status_code)
        except Exception as e:
            print("An error occurred while fetching sessions:", str(e))

    def switch_screen(self, screen_name):
        self.manager.current = screen_name
        print(f"Switching to screen: {screen_name}")