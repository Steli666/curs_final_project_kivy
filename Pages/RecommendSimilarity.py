from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
import csv

class RecommendSimilarity(Screen):
    # def on_enter(self):
    #     self.load_movies()

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
                OneLineListItem(text=movie, on_release=lambda x, m=movie: self.show_movie_detail(m))
            )

    def filter_movies(self, query):
        self.load_movies()
        filtered_movies = [movie for movie in self.movies if query.lower() in movie.lower()]
        self.display_movies(filtered_movies)

    def search(self, query):
        self.filter_movies(query)

    def show_movie_detail(self, title):
        app = MDApp.get_running_app()
        app.root.current = 'movie_detail'
        app.root.get_screen('movie_detail').display_movie_detail(title)