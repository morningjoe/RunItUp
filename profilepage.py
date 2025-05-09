import os
import sys

from kivy.core.window import Window
from kivy import __version__ as kv__version__
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd import __version__


from materialyoucolor import __version__ as mc__version__



# writing kv lang 
KV = ''' 
# declaring layout/screen 
MDScreen:
    BoxLayout:
        orientation: "vertical"

        # Main scrollable area
        MDScrollView:
            MDBoxLayout:
                id: main_scroll
                orientation: "vertical"
                adaptive_height: True
                padding: "10dp"
                spacing: "10dp"

                MDLabel:
                    text: "Scrollable content goes here"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "More scrollable content"
                    size_hint_y: None
                    height: self.texture_size[1]

        # Fixed bottom navigation bar with full width
        MDBottomNavigation:
            panel_color: 1, 1, 1, .4

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Settings'
                icon: './icons/setting.webp'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Search'
                icon: './icons/search.png'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Profile'
                icon: './icons/profile.png'
    
                                 
'''
  
# App class 
class Test(MDApp): 
    
  
    def build(self): 
        
        # this will load kv lang 
        screen = Builder.load_string(KV) 
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        # returning screen 
        return screen 
    Window.size = [dp(350), dp(600)]
        

Test().run() 