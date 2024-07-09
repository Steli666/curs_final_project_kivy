import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
import csv
from Pages.Home import Home
from All import token_store, logout

class RecommendRating(Screen):
    def on_enter(self):
        Home.update_right_action_items(self)

    def on_leave(self):
        self.ids.search_field.text = ""

    def fetch_recommendations(self, movie_title):
        token = token_store.get("vars")["token"]
        headers = {"Authorization": f"{token}"}
        response = requests.get(f"http://127.0.0.1:8000/api/rec_rat?movie={movie_title}", headers=headers)

        if response.status_code == 200:
            recommendations = response.json()["recommendations"]
            self.display_recommendations(recommendations)
        else:
            print(response.status_code)
            print("Failed to fetch recommendations")

    def display_recommendations(self, recommendations):
        self.ids.movie_list.clear_widgets()
        for recommendation in recommendations:
            item = OneLineListItem(text=f"{recommendation['title']} - Correlation: {recommendation['Correlation']:.2f}")
            self.ids.movie_list.add_widget(item)

    def search(self, query):
        self.fetch_recommendations(query)

    def logout(self):
        logout(self)
        self.manager.current = 'home'