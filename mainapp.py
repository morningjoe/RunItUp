from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import profilepage
# writing kv lang 
KV = ''' 
# declaring layout/screen 
WindowManager:
    Home:
    profile:
<Home>
    MDScreen: 
    
        # this will create a space navigation bottom 
        MDBottomNavigation: 
            panel_color: 1,1,1,.4
            #text_color_active: 0,0,0,1
            id: bottom_nav
            on_switch_tabs: app.on_switch_tabs(*args)
    
            # this will create a navigation button on the bottom of screen 
            MDBottomNavigationItem: 
                name: 'screen 1' 
                text: 'Settings' 
                icon: './icons/setting.webp' 
    
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

        
'''
  
# App class 
class Test(MDApp): 
    def on_switch_tabs(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        def on_switch_tabs(
        self,
        bar: MDBottomNavigation,
        item: MDBottomNavigationItem,
        item_icon: str,
        item_text: str,
    ):
            if item_text == 'Profile':
                return profilepage.Test.build()

    def build(self):  
        # this will load kv lang 
        screen = Builder.load_string(KV) 
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        # returning screen 
        return screen
        

Test().run() 