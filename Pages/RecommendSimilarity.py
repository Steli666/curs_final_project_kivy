import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
import csv
from Pages.Home import Home
from All import token_store, logout

class RecommendSimilarity(Screen):
    def on_enter(self):
        Home.update_right_action_items(self)
        # self.load_movies()

    def load_movies(self):
        self.movies = []
        with open('movies1.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                title = row[1]
                self.movies.append(title)
        self.display_movies(self.movies)

    def display_movies(self, movies):
        self.ids.movie_list.clear_widgets()
        for movie in movies:
            self.ids.movie_list.add_widget(
                OneLineListItem(text=movie)
            )

    def filter_movies(self, query):
        url = f"http://127.0.0.1:8000/api/rec_sim?movie={query}"
        headers = {"Authorization": token_store.get("vars")["token"]}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                recommendations = response.json().get("recommendations", [])
                self.display_movies(recommendations)
            else:
                print("Error fetching recommendations:", response.status_code)
        except Exception as e:
            print("An error occurred while fetching recommendations:", str(e))

    def search(self, query):
        self.filter_movies(query)

    def logout(self):
        logout(self)
        self.manager.current = 'home'