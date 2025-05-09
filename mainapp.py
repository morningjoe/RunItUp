from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
import profilepage
from profilepage import Screen_2
from kivy.core.window import Window
from kivy.metrics import dp

Builder.load_file('profile.kv')
Builder.load_file('home.kv')

class Screen_1(MDScreen):
    pass

class Manager(ScreenManager):
    screen_1 = ObjectProperty(None)
    screen_2 = ObjectProperty(None)
    pass
# App class
class Test(MDApp): 
    dialog = None
    def profileSwitch(self, *args):
        self.root.current = "screen_2"
        
    def build(self):  
        sm = Manager()
        sm.add_widget(Screen_1(name = 'screen_1'))
        sm.add_widget(Screen_2(name = 'screen_2'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        sm.current = 'screen_1'

        # returning screen 
        return sm
    Window.size = [dp(350), dp(600)]
    

Test().run() 