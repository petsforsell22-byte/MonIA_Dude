from kivy.app import App
from kivy.uix.button import Button

class DudeApp(App):
    def build(self):
        return Button(text="DUDE IA ACTIVE")

if __name__ == "__main__":
    DudeApp().run()

