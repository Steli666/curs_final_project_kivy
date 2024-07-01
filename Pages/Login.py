import re
from tkinter import Widget
import requests
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from All import token_store

class Login(Screen):
    def next(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")

    def show_error(self, widget):
        widget.error = True
        widget.background_color = get_color_from_hex("#FF0000")
    def clear_error(self, widget):
        widget.error = False
        widget.background_color = get_color_from_hex("#FFFFFF")

    def validate_inputs(self):
        valid = True
        username = self.ids.username
        password = self.ids.password
        if not username.text:
            self.show_error(username)
            valid = False
        else:
            self.clear_error(username)
        if not password.text:
            self.show_error(password)
            valid = False
        else:
            self.clear_error(password)
        return valid
    def login(self):
        if not self.validate_inputs():
            return

        username = self.ids.username.text
        password = self.ids.password.text
        url = "http://127.0.0.1:8000/api/login"
        payload = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                token_response = response.json()
                token_store.put("vars", token="Token " + token_response.get("token"))
                self.manager.current = "home"
            else:
                dialog = MDDialog(
                    title="Wrong username or password",
                    text="Please input correct information",
                    size_hint=(0.8, 0.4),
                    background_color=(1, 1, 1, 0)
                )
                dialog.elevation = 0
                dialog.open()
                print("Failed to fetch sessions. Status code:", response.status_code)
        except Exception as e:
            print("An error occurred while fetching sessions:", str(e))