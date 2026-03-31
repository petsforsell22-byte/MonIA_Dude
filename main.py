from kivy.app import App
from kivy.uix.label import Label

class DudeApp(App):
    def build(self):
        return Label(text="DUDE IA : SYSTÈME DÉCHAÎNÉ ET OPÉRATIONNEL")

if __name__ == '__main__':
    DudeApp().run()

