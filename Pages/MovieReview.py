import pandas as pd
import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from Pages.Home import Home
from All import token_store, logout

class MovieReview(Screen):
    def on_enter(self):
        Home.update_right_action_items(self)

    def on_leave(self):
        self.ids.menu_for_movies.text = "Rate this movie"

    def display_movie_detail(self, title):
        self.ids.movie_title.text = title

    def drop_down_menu_for_movies(self):
        self.menu_list_for_movies = [{
            "viewclass": "OneLineListItem",
            "text": "1",
            "on_release": lambda x="1": self.movie_title(x)
            },
            {"viewclass": "OneLineListItem",
             "text": "2",
             "on_release": lambda x="2": self.movie_title(x)
             },
            {"viewclass": "OneLineListItem",
             "text": "3",
             "on_release": lambda x="3": self.movie_title(x)
             },
            {"viewclass": "OneLineListItem",
             "text": "4",
             "on_release": lambda x="4": self.movie_title(x)
             },
            {"viewclass": "OneLineListItem",
             "text": "5",
             "on_release": lambda x="5": self.movie_title(x)
             }
        ]
        self.menu1 = MDDropdownMenu(
            caller=self.ids.menu_for_movies,
            items=self.menu_list_for_movies,
            width_mult=4
        )
        self.menu1.open()

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.8, 0.4)
        )
        dialog.elevation = 0
        dialog.open()

    def submit_review(self):
        token = token_store.get("vars")["token"]
        headers = {"Authorization": f"{token}"}
        movie_title = self.ids.movie_title.text
        rating = self.ids.menu_for_movies.text

        if not movie_title or rating not in ["1", "2", "3", "4", "5"]:
            self.show_dialog(title="Input Error!", message="Rating is required!")
            return

        movie_ratings = pd.read_csv("movies_ratings.csv")
        matched_row = movie_ratings[movie_ratings['title'] == movie_title].iloc[0]
        movie_id = matched_row['movieId']
        genres = matched_row['genres']


        data = {
            "movie": {"movieId": int(movie_id),
            "title": movie_title,
            "genres": genres},
            "rating": {"rating": float(rating)}
        }

        response = requests.post(
            "http://127.0.0.1:8000/api/add_review",
            json=data,
            headers=headers
        )

        if response.status_code == 201:
            self.show_dialog(title="Success!", message="Review created successfully")
            print("Review created successfully")
        else:
            self.show_dialog(title="SubmitError!", message="You can't rate the same movie again!")

    def movie_title(self, movie_title):
        self.ids.menu_for_movies.text = movie_title

    def logout(self):
        logout(self)
        self.manager.current = 'home'