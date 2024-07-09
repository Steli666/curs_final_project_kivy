from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
import csv
from Pages.Home import Home
from All import token_store, logout

class AddReview(Screen):
    def on_enter(self):
        Home.update_right_action_items(self)
        self.load_movies()

    def on_leave(self):
        self.ids.search_field.text = ""

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
        for index, movie in enumerate(movies):
            if index == 0:
                self.ids.movie_list.add_widget(OneLineListItem(text=movie))
            else:
                self.ids.movie_list.add_widget(
                    OneLineListItem(text=movie, on_release=lambda x, m=movie: self.show_movie_detail(m))
                )

    def filter_movies(self, query):
        filtered_movies = [movie for movie in self.movies if query.lower() in movie.lower()]
        self.display_movies(filtered_movies)

    def search(self, query):
        self.filter_movies(query)

    def show_movie_detail(self, title):
        app = MDApp.get_running_app()
        app.root.current = 'movie_detail'
        app.root.get_screen('movie_detail').display_movie_detail(title)

    def logout(self):
        logout(self)
        self.manager.current = 'home'