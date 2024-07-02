from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from Pages.Home import Home
from All import token_store, logout

class MovieReview(Screen):
    def on_enter(self):
        Home.update_right_action_items(self)

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

    def movie_title(self, movie_title):
        self.ids.menu_for_movies.text = movie_title

    def logout(self):
        logout(self)
        self.manager.current = 'home'