from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty
from kivy.core.window import Window
from Pages.Home import Home
import math
import requests
from kivy.config import Config
from kivy.properties import get_color_from_hex
from kivy.storage.jsonstore import JsonStore
import re
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.navigationdrawer import MDNavigationDrawerLabel

from Pages.Register import Register
from Pages.Login import Login
from Pages.AddReview import AddReview
from Pages.RecommendSimilarity import RecommendSimilarity
from Pages.RecommendRating import RecommendRating
from Pages.MovieReview import MovieReview

class Base:
    pass

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "900"
        Builder.load_file("Home.kv")
        Builder.load_file("Register.kv")
        Builder.load_file("AddReview.kv")
        Builder.load_file("RecommendSimilarity.kv")
        Builder.load_file("RecommendRating.kv")
        Builder.load_file("MovieReview.kv")
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Register(name='register'))
        sm.add_widget(Login(name='login'))
        sm.add_widget(AddReview(name='add_review'))
        sm.add_widget(RecommendSimilarity(name='recommend_similarity'))
        sm.add_widget(RecommendRating(name='recommend_rating'))
        sm.add_widget(MovieReview(name='movie_detail'))
        return sm

Example().run()