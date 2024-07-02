import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from Pages.Home import Home
from All import token_store, logout

class MyReviews(Screen):
        def on_enter(self):
            Home.update_right_action_items(self)
            self.fetch_reviews()

        def fetch_reviews(self):
            token = token_store.get("vars")["token"]
            headers = {"Authorization": f"{token}"}
            response = requests.get("http://127.0.0.1:8000/api/user_reviews", headers=headers)

            if response.status_code == 200:
                reviews = response.json()
                self.display_reviews(reviews)
            else:
                print("Failed to fetch reviews")

        def display_reviews(self, reviews):
            review_list = self.ids.review_list
            review_list.clear_widgets()
            for review in reviews:
                item = OneLineListItem(text=f"{review['movie_title']} - Rating: {review['rating']}")
                review_list.add_widget(item)

        def logout(self):
            logout(self)
            self.manager.current = 'home'