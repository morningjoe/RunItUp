import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


# import packages 
from kivy.lang import Builder 
from kivymd.app import MDApp 
  
# writing kv lang 
KV = ''' 
# declaring layout/screen 
MDScreen: 
  
    # this will create a space navigation bottom 
    MDBottomNavigation: 
        panel_color: 1,1,1,.4
        #text_color_active: 0,0,0,1
  
        # this will create a navigation button on the bottom of screen 
        MDBottomNavigationItem: 
            name: 'screen 1' 
            text: 'Settings' 
            icon: './icons/setting.webp' 
  
            # this will be triggered when screen 1 is selected 
            # creates a label 
            MDLabel: 
                text: 'You have selected Camera' 
                halign: 'center' 
  
        # this will create a navigation button on the bottom of screen 
        MDBottomNavigationItem: 
            name: 'screen 2' 
            text: 'Search' 
            icon: './icons/search.png' 
  
            # this will be triggered when screen 2 is selected 
            # creates a label 
            MDLabel: 
                text: 'You have selected Microphone' 
                halign: 'center' 
  
        # this will create a navigation button on the bottom of screen 
        MDBottomNavigationItem: 
            name: 'screen 3' 
            text: 'Profile' 
            icon: './icons/profile.png' 
  
            # this will be triggered when screen 3 is selected 
            # creates a label 
            MDLabel: 
                text: 'You have selected Wi-Fi' 
                halign: 'center' 
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
        

Test().run() 